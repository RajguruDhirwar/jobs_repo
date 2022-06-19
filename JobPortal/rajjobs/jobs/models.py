from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    eligibility = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Banglorejbs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    eligibility = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Punejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    eligibility = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
