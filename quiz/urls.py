from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.site_register, name="registration"),
    path("login/", views.site_login, name="login"),
    path("home/", views.home_page, name="home_page"),
    path("quiz/", views.quiz_page, name="quiz_page"),
    path("quiz_rus/", views.quiz_page_rus, name="quiz_page_rus"),
    path("language/", views.tilni_tanlash, name="tilni_tanlash"),
    path("", views.first_page, name="first_page"),
]
