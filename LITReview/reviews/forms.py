from django import forms
from django.utils.safestring import mark_safe

from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {
            "title": "Titre",
            "description": "Description",
            "image": "Image"
        }


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'body', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[
                (0, "- 0"),
                (1, "- 1"),
                (2, "- 2"),
                (3, "- 3"),
                (4, "- 4"),
                (5, "- 5")],
            )
        }
        labels = {
            "headline": "Titre de la critique",
            "body": "Corps",
            "rating": "Note"
        }


class FollowForm(forms.Form):
    followed_user = forms.CharField(
        required=True,
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom d'utilisateur"
            }),
        label=""
    )
