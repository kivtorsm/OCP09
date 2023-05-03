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
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Titre de la demande de critique',
                'class': "form-control"
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Texte de la demande de critique',
                'class': "form-control",
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': "form-control"
            })
        }


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'body', 'rating']
        widgets = {
            'rating': forms.RadioSelect(
                choices=[
                    (0, "0"),
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5")],
                attrs={
                    'class': "ms-4",
                },
            ),
            'headline': forms.TextInput(attrs={
                'placeholder': 'Titre de la critique',
                'class': "form-control"
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Texte',
                'class': "form-control",
                'rows': 5,
            })
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
                "placeholder": "Nom d'utilisateur",
                "class": "col-lg-8"
            }),
        label=""
    )
