from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('signup', views.signup_page, name='signup_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
]
