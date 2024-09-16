from django.shortcuts import render, redirect
from tickets.models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

@login_required
def home_user(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        ticket = Ticket(title=title, description=description, priority=priority, created_by=request.user)
        ticket.save()

        # Añadir mensaje de éxito
        messages.success(request, 'Ticket creado con éxito.')
        return redirect('home_user')
    
    return render(request, 'tickets/home_user.html')

# Lógica de logout
def logout_view(request):
    logout(request)
    return redirect('login')
