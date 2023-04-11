from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    email = forms.EmailField(max_length=200, label=' E-mail')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
