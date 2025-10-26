from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "autofocus": True,
            "placeholder": "you@example.com",
            "class": "form-control"
        })
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Ваш пароль",
            "class": "form-control"
        })
    )
