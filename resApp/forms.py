from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username...'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email...'
            }),

            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password...'

            }),

            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Re-enter password...'
            })
        }

