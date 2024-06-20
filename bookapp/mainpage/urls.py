from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('signup', views.signup_page, name='signup_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
    path('get_raiting', views.get_raiting, name='get_raiting'),
    path('get_rating_s/<int:id>', views.get_rating_s, name='get_rating_s'),
    path('bookdetail/<int:id>', views.detail_view, name='detail_view'),
    path('get_reviews/<int:id>', views.get_reviews, name='get_reviews'),
    path('add_book/', views.add_book, name='add_book'),
]
