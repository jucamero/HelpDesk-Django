from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Página del Home para usuarios autenticados
@login_required
def home_user(request):
    if request.user.is_superuser:
        return redirect('admin_user')  # Redirige a la vista de administración para superusuarios

    # Redirige según el rol del usuario
    if request.user.role == 'user':
        return render(request, 'tickets/home_user.html')
    elif request.user.role == 'support1':
        return render(request, 'tickets/home_support1.html')
    elif request.user.role == 'support2':
        return render(request, 'tickets/home_support2.html')

    # En caso de que el rol no coincida con ninguno de los definidos
    return redirect('login')  # O cualquier otra página de error o logout











"""
# Página del Home para usuarios autenticados
@login_required
def home_user(request):
    if request.user.is_superuser:
        return redirect('admin_user')  # Redirige a la vista de administración para superusuarios
    return render(request, 'tickets/home_user.html') # Muestra la vista de home_user cuando el usuario es = user
    """

# Lógica de logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al inicio de sesión después del logout