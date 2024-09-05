from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
#Imports para el home:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#Imports para el Home logout:
from django.contrib.auth import logout
from django.shortcuts import redirect


#Vista del registro
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # O redirige donde prefieras
    else:
        form = CustomUserCreationForm()
    return render(request, 'tickets/register.html', {'form': form})

#Vista del login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la vista 'home'
        else:
            return render(request, 'tickets/login.html', {'error': '¡Credenciales incorrectas, intenta de nuevo!'})
    return render(request, 'tickets/login.html')



#Pagina del Home
#Login 
@login_required
def home(request):
    return render(request, 'tickets/home.html')


#Logout - Logica que redirecciona al login al presionar logout
def logout_view(request):
    logout(request)
    return redirect('login')
