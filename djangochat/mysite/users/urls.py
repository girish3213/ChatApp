from django.urls import path
from . import  views


app_name = 'users'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'), 
    path('about/', views.about_view, name='about'),
]