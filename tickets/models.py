from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'Usuario'),
        ('support1', 'Soporte Nivel 1'),
        ('support2', 'Soporte Nivel 2'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Leve'),
        ('medium', 'Moderada'),
        ('high', 'Grave'),
        ('urgent', 'Urgente'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, default='En proceso')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, related_name='assigned_tickets', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
