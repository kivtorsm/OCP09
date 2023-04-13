from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'reviews/home.html', context)

