from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    senha = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)

    def __str__(self):
        return f"\nName: {self.name}\n email: {self.email}\n senha: {self.senha}\n tipo: {self.tipo}"

