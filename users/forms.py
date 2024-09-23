from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'rut')
    list_filter = ('user_type',)
    search_fields = ('user__username', 'user__email', 'rut')

    # Permite que solo los superusuarios cambien el tipo de usuario
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            # Evita que usuarios no administradores cambien el user_type
            form.cleaned_data['user_type'] = obj.user_type
        super().save_model(request, obj, form, change)

admin.site.register(Profile, ProfileAdmin)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico')
    first_name = forms.CharField(max_length=30, required=False, label='Nombre')
    last_name = forms.CharField(max_length=30, required=False, label='Apellido')
    rut = forms.CharField(max_length=12, label='RUT', help_text='Ingrese su RUT sin puntos ni guiones')
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES, label='Tipo de Usuario')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'rut', 'user_type', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.rut = self.cleaned_data['rut']
            profile.user_type = self.cleaned_data['user_type']
            profile.save()
        return user