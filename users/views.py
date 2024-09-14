from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def especialistas(request):
    return render(request, 'especialistas/especialistas.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña no válidos')
    return render(request, 'navegacion/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado con éxito.')
            return redirect('home')
        
    else:
        form = UserRegisterForm()
        
    return render(request, 'navegacion/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

