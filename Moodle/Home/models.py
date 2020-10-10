from django.db import models

# Create your models here.
class Cursos(models.Model):
    nome= models.CharField(max_length=100)
    areaDc= models.CharField(max_length=100)

