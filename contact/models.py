from django.db import models
from django.utils import timezone

# Create your models here.
# O ID é automaticamente gerado pelo Django

class Contact(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.name} {self.lastname}'
