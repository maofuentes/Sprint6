from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import User

class UsuarioSignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)

    GRUPOS_CHOICES = [
        ('grupo1', 'Adminitrador'),
        ('grupo2', 'Usuarios'),
    ]
    grupo = forms.ChoiceField(label='grupo', choices=GRUPOS_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'grupo']
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.save()
        return user
