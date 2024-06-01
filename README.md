**Описание**
API для Yatube (cоциальная сеть). У неаутентифицированных пользователей доступ к API только на чтение (за исключением эндпоинта /follow/). Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.
Документация к проекту находится по адресу http://127.0.0.1:8000/redoc/ и представлена в формате Redoc.

**Установка**
Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/ViolettaValieva/api_final_yatube.git`
`cd api_final_yatube`
Cоздать и активировать виртуальное окружение:

`python3 -m venv env`
`source env/bin/activate`
`python3 -m pip install --upgrade pip`
Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`
Выполнить миграции:

`python3 manage.py migrate`
Запустить проект:

`python3 manage.py runserver`

