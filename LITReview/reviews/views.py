from itertools import chain

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from . import models, forms


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

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        # TODO: Question, comment faire si le nom de champ n'est pas identique ?
        reverse=True
    )

    context = {
        'tickets_and_reviews': tickets_and_reviews,
        'page': 'home',
        'user': request.user,
    }
    return render(request, 'reviews/home.html', context)


@login_required()
def posts(request):

    reviews = models.Review.objects.filter(user=request.user)

    tickets = models.Ticket.objects.filter(
        user=request.user)

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    context = {
        'tickets_and_reviews': tickets_and_reviews,
        'page': 'my_posts',
        'user': request.user,
    }
    return render(request, 'reviews/posts.html', context)


@login_required()
def new_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        post = request.POST.copy()
        post['user'] = request.user.id
        ticket_form = forms.TicketForm(post)
        if ticket_form.is_valid():
            validated_form = ticket_form.save(commit=False)
            validated_form.user = request.user
            validated_form.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'user': request.user,
    }
    return render(request, 'reviews/new_ticket.html', context=context)


@login_required()
def follows(request):
    pass

