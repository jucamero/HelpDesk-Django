from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from django.contrib.auth import logout

@login_required
def home_support1(request):
    if request.user.role != 'support1':
        return redirect('login')

    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        new_status = request.POST.get('status')
        if ticket_id and new_status:
            ticket = get_object_or_404(Ticket, id=ticket_id)
            if ticket.status in ['sin_asignar', 'en_proceso', 'escalado', 'devuelto']:
                ticket.status = new_status
                ticket.save()
            return redirect('home_support1')

    tickets = Ticket.objects.filter(status__in=['sin_asignar', 'en_proceso', 'escalado', 'devuelto', 'terminado'])
    return render(request, 'tickets/home_support1.html', {'tickets': tickets})

# Lógica de logout
def logout_view(request):
    logout(request)
    return redirect('login')
