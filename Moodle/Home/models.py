from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)

    def __str__(self):
        return f"Name: {self.name}\n email: {self.name}\n password: {self.name}"

