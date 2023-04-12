from django import forms


class LoginForm(forms.Form):

    USER = 'USER'

    ROLE_CHOICES = (
        (USER, 'Utilisateur'),
    )
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
