from django import forms

from . import models


class TicketForm(forms.modelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'user', 'image', 'time_created']


class ReviewForm(forms.modelForm):
    class Meta:
        model = models.Review
        fields = ['ticket', 'rating', 'headline', 'body', 'user', 'time_created']


