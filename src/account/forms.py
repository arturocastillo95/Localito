from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Utiliza un correo electronico valido', label='Correo Electronico', widget=forms.EmailInput(attrs={'class':'input','autocomplete':'username'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'input','autocomplete':'new-password'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class':'input','autocomplete':'new-password'}))

    class Meta:
        model = Account
        fields = ('email',)
