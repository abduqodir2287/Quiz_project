from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.site_register, name="registration"),
    path("", views.site_login, name="login"),
    path("home/", views.home_page, name="home_page"),
    path("quiz/", views.quiz_page, name="quiz_page"),
    # path("con/", views.con, name="congrat")
    # path('addquiz/', views.addquiz, name='addquiz')
]
