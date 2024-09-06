from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Vista del login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_user')  # Redirige a la vista 'home_user'
        else:
            return render(request, 'tickets/login.html', {'error': '¡Credenciales incorrectas, intenta de nuevo!'})
    return render(request, 'tickets/login.html')