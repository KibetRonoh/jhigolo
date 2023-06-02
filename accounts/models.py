from django.db import models
from django.contrib.auth.models import AbstractUser, User
# from django.utils.html import escape, make_safe


class User(AbstractUser):
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    body = models.CharField(max_length=20)
    height = models.CharField(max_length=20, default='medium')
    gender = models.CharField(max_length=20, default='medium')
    outcall_price = models.IntegerField()
    incall_price = models.IntegerField()
    about = models.TextField(max_length=100, default='about me')
    vip = models.BooleanField(default=False)
    regular = models.BooleanField(default=True)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')