from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from users.models import Profile 
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico')
    first_name = forms.CharField(max_length=30, required=False, label='Nombre')
    last_name = forms.CharField(max_length=30, required=False, label='Apellido')
    rut = forms.CharField(max_length=12, label='RUT', help_text='Ingrese su RUT sin puntos ni guiones')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'rut', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.rut = self.cleaned_data['rut']
            profile.save()
        return user