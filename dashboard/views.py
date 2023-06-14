from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from ticket.models import Ticket
from ticket.forms import CreateTicketForm, UpdateTicketForm
from users.models import User
from django.contrib.auth.decorators import login_required



#Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def dashboard(request):
    # Get the username
    username = request.user.username

    # Retrieve the necessary statistics based on the user's role
    if request.user.is_customer:
        total_tickets = Ticket.objects.filter(created_by=request.user).count()
        resolved_tickets = Ticket.objects.filter(created_by=request.user, is_resolved=True).count()
        open_tickets = Ticket.objects.filter(created_by=request.user, is_resolved=False).count()
        context = {
            'username': username,
            'total_tickets': total_tickets,
            'resolved_tickets': resolved_tickets,
            'open_tickets': open_tickets,
        }
    elif request.user.is_engineer:
        total_tickets_on_queue = Ticket.objects.filter(assigned_to=request.user, is_resolved=False).count()
        total_resolved_tickets_by_engineer = Ticket.objects.filter(assigned_to=request.user, is_resolved=True).count()
        total_accepted_tickets = Ticket.objects.filter(assigned_to=request.user, accepted_date__isnull=False).count()
        context = {
            'username': username,
            'total_tickets_on_queue': total_tickets_on_queue,
            'total_resolved_tickets_by_engineer': total_resolved_tickets_by_engineer,
            'total_accepted_tickets': total_accepted_tickets,
            # Add engineer-specific context variables here
        }
    else:
        # Handle other user roles here
        context = {
            'username': username,
            # Add context variables for other roles here
        }

    return render(request, 'dashboard/dashboard.html', context)