from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
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
        ticket_form = forms.TicketForm(request.POST, request.FILES)
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


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        elif 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'reviews/edit_ticket.html', context=context)


@login_required()
def create_ticket_plus_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            ticket.save()
            review.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'reviews/create_ticket_plus_review.html', context=context)


@login_required
def create_review(request, ticket_id):
    review_form = forms.ReviewForm()
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'reviews/create_review.html', context=context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    ticket = get_object_or_404(models.Ticket, id=review.ticket.id)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        elif 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        'ticket': ticket,
    }
    return render(request, 'reviews/edit_review.html', context=context)


@login_required()
def follows(request):
    pass

