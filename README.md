Сайт с навигацией, написан по заказу на фрилансе, в команде frontend and backend разработчиками, в данном заказе за фронтенд разработку отвечал я сам
1. Сначало устанавливаем Python 3.9 - желательно его
2. В командной строке впишите venv\Scripts\activate
3. cd org
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver

По данному пути: http://127.0.0.1:8000/admin будет доступна админка(только для вас, как админу сайта).
После приобритения хостинга нужно заменить http://127.0.0.1:8000 на свой домен

Login admin: AdminAbove
Password admin: Pr-5Lh#SQ-Rt


После всех этих действий зайдите в файл settings.py и в переменную CSRF_TRUSTED_ORIGINS вставьте свой домен
Должно выглядеть так CSRF_TRUSTED_ORIGINS = ['свой домен']
