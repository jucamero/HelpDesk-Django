#Logica para ver los tickets creados en otra url cuando el user da click en ver tickets creados en home_user
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket

@login_required
def home_user_tickets(request):
    if request.method == 'POST':
        # Manejar la edición de ticket
        if 'ticket_id' in request.POST:
            ticket_id = request.POST['ticket_id']
            ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)
            ticket.title = request.POST['title']
            ticket.description = request.POST['description']
            ticket.priority = request.POST['priority']
            ticket.save()
            return redirect('home_user_tickets')

        # Manejar la eliminación de ticket
        if 'delete_ticket_id' in request.POST:
            ticket_id = request.POST['delete_ticket_id']
            ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)
            ticket.delete()
            return redirect('home_user_tickets')

    tickets = Ticket.objects.filter(created_by=request.user)
    return render(request, 'tickets/home_user_tickets.html', {'tickets': tickets})

@login_required
def delete_ticket(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)
        ticket.delete()
    return redirect('home_user_tickets')
