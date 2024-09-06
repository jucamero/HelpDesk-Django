from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Página del Home
@login_required
def home_user(request):
    return render(request, 'tickets/home_user.html')

# Lógica de logout
def logout_view(request):
    logout(request)
    return redirect('login')