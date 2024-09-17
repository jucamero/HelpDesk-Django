from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'Usuario'),
        ('support1', 'Soporte Nivel 1'),
        ('support2', 'Soporte Nivel 2'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username

class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Leve'),
        ('medium', 'Moderada'),
        ('high', 'Grave'),
        ('urgent', 'Urgente'),
    ]

    STATUS_CHOICES = [
        ('sin_asignar', 'Sin asignar'),
        ('en_proceso', 'En proceso'),
        ('escalado', 'Escalado'),
        ('terminado', 'Terminado'),
        ('devuelto', 'Devuelto'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='sin_asignar')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_created')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='tickets_assigned')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title