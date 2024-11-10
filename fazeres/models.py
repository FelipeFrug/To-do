# fazeres/models.py
from django.db import models

class ToDo(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('C', 'Completa'),
    ]
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text