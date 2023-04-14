from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from . import models


@login_required
def home(request):
    # get list of followed users to be filtered
    followed_users = models.UserFollows.objects.filter(user=request.user).values('followed_user_id')

    reviews = models.Review.objects.filter(
        Q(user__in=followed_users) | Q(user=request.user) | Q(ticket__user=request.user)
    )

    tickets = models.Ticket.objects.filter(
        Q(user__in=followed_users) | Q(user=request.user)
    ).exclude(review__in=reviews)

    context = {
        'tickets': tickets,
        'reviews': reviews
    }
    return render(request, 'reviews/home.html', context)

