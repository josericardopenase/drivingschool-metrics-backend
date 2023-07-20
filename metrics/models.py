from django.db import models

# Create your models here.
class DgtTests(models.Model):
    name = models.CharField(max_length=255)
    autoescuela = models.CharField(max_length=255)
    aprobados = models.IntegerField()
    presentados = models.IntegerField()