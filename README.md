Для запуска проекта необходимо :
    1. Сделайтке клон репозитория 
        -если у вас установлен git, то введите в терминале команду:
            -если настроен ssh: git clone git@github.com:Guljigit001/site-django.git
            -если настроен https: git clone https://github.com/Guljigit001/site-django.git
    2. Создайте виртуальное окружение
    - если у вас установлен python3, то введите в терминале команду:
        - python3 -m venv venv
    !!! ВАЖНО !!!
    - если в вас WINDOWS, уточните создание виртуального окружения
        - https://docs.python.org/3/library/venv.html

3. Активируйте виртуальное окружение
    - если у вас установлен python3, то введите в терминале команду:
        - source venv/bin/activate
    !!! ВАЖНО !!!
    - если в вас WINDOWS, уточните активацию виртуального окружения
        - https://docs.python.org/3/library/venv.html

4. Установите зависимости
    - введите в терминале команду: pip install -r req.txt

5. Сделайте миграции
    - введите в терминале команду: python manage.py migrate

6. Запустите проект
    - введите в терминале команду: python manage.py runserver

7. Создайте суперпользователя
    - введите в терминале команду: python manage.py createsuperuser         