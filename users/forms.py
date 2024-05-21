# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    home = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'home')
