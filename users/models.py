from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('admin', 'Administrador'),
        ('patient', 'Paciente'),
        ('specialist', 'Especialista'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='patient')
    rut = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.user.username