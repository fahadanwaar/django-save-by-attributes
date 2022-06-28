from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

