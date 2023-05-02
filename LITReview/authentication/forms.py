from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Nom d\'utilisateur',
            }
        )
    )
    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Mot de passe',
            }
        ),
        label='')


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': "Nom d'utilisateur",
                'class': "form-control"
            })
        }
        labels = {
            "username": "",
            "password1": ""
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['class'] = 'form-control'
            self.fields[fieldname].labels = ''


        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer mot de passe'


