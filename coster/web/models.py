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
    type = models.CharField(max_length=100)
    theta0 = models.FloatField()
    theta1 = models.FloatField()
    theta2 = models.FloatField()
    theta3 = models.FloatField()
    theta4 = models.FloatField()

class middleman(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dong = models.CharField(max_length=100)
    img = models.CharField(max_length=100)