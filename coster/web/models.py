from django.db import models

class user(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    power = models.IntegerField()

class consulting(models.Model):
    si = models.CharField(max_length=100)
    gu = models.CharField(max_length=100)
    dong = models.CharField(max_length=100, primary_key=True)
    theta = models.FloatField()