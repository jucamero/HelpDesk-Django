from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from django.contrib.auth import logout

@login_required
def home_support2(request):
    if request.user.role != 'support2':
        return redirect('login')  # Redirige a login si el usuario no es soporte nivel 2

    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        new_status = request.POST.get('status')
        if ticket_id and new_status:
            ticket = get_object_or_404(Ticket, id=ticket_id)
            if ticket.status == 'escalado':
                ticket.status = new_status
                ticket.save()
            return redirect('home_support2')

    tickets = Ticket.objects.filter(status__in=['escalado', 'terminado'])  # Soporte nivel 2 ve tickets escalados y terminados
    return render(request, 'tickets/home_support2.html', {'tickets': tickets})

# Lógica de logout
def logout_view(request):
    logout(request)
    return redirect('login')