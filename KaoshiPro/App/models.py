from django.db import models

# Create your models here.

#用户表
class User(models.Model):
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50)

#商品表
class Shangpin(models.Model):
    title = models.CharField(max_length=50)
    impage = models.CharField(max_length=255)
    price = models.FloatField(default=100.0)
    type = models.CharField(max_length=20)


