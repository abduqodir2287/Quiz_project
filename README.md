# https://signup.heroku.com    shu saytdan ro'yxatdan o'tamiz va kerakli ma'lumotlarni to'ldiramiz
# https://cli-assets.heroku.com/heroku-x64.exe dasturni yuklab olamiz

_________________________________________________________________
# Kerakli packages ornatib olamiz
# pip install Django==4.2 
# pip install gunicorn
# pip install whitenoise
_________________________________________________________________

# Agar whitenoise ni qanday ishlatishni bilmasangiz!!
# Mana bu ssilka orqali bilib olishingiz mumkin 👇👇
# https://www.w3schools.com/django/django_static_whitenoise.php
_________________________________________________________________

# Procfile ni yaratamiz va ichiga 
#    web: gunicorn Your_project_name.wsgi --log-file -
#    'Your_project_name' orniga projectingizni nomini yozing
_________________________________________________________________

# runtime.txt ni yaratamiz va ichiga 
#    python-3.11.2
#    Siz o'zingizni Python versiyangizni yozasiz
_________________________________________________________________

# Terminal
# pip freeze > requirements.txt
# requirements.txt nomli fayl yaratiladi va uning ichida
# Barcha install qilingan packages lar turadi
_________________________________________________________________

# Terminal
# git init
# git add -A
# git commit -m "Commit for Heroku"

# heroku login
# heroku create 
# herokudan app yaratiladi va shu nomni beriladi
# heroku git:remote -a app_name
# git push heroku master
# Bot herokuga yuklandi !!
_____________________________________________________

# heroku run python manage.py migrate
# heroku run python manage.py createsuperuser
# Tepadagi buyruq bilan Superuser yaratamiz
_____________________________________________________

# Agar barchasini tog'ri bajargan bolsangiz tabriklayman!!
# Siz endi saytingizni bemalol ishlatishingiz mumkin.

_____________________________________________________