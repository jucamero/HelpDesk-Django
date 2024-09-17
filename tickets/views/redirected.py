
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Página del Home para usuarios autenticados
@login_required
def redirected(request):
    if request.user.is_superuser:
        return redirect('admin_user')  # Redirige a la vista de administración para superusuarios

    # Redirige según el rol del usuario
    if request.user.role == 'user':
        return redirect('home_user')
    elif request.user.role == 'support1':
        return redirect('home_support1')
    elif request.user.role == 'support2':
        return redirect('home_support2')

    # En caso de que el rol no coincida con ninguno de los definidos
    return redirect('login')  # O cualquier otra página de error o logout


# Lógica de logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al inicio de sesión después del logout
