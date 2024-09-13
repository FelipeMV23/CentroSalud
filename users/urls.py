from django.contrib import admin
from django.urls import path, include
from .views import register
from users import views

urlpatterns = [
    path('especialistas/', views.especialistas, name='especialistas'),
    path('registrarse/', register, name='register'),
    path('login/', views.user_login, name='login'),
    
]