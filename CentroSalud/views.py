from django.shortcuts import render, redirect
from CentroSalud.context_processors import nav_items
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'navegacion/navbar.html', nav_items('nav_items'))

