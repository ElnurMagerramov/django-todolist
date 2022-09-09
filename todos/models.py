from django.db import models

# Create your models here.

class Todos(models.Model):
    name=models.CharField(max_length=50)


class Got(models.Model):
    name=models.CharField(max_length=50)

class MyModel(models.Model):
    Domain = models.CharField(max_length=50)
    Votes = models.CharField(max_length=50)
    Dates = models.CharField(max_length=50)
    Links = models.CharField(max_length=50)

    wage = models.FloatField()