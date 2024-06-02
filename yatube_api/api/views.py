from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)
from posts.models import Group, Post, User


class ListCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        return User.objects.get(username=self.request.user.username).follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
