from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=1000)
    customer_address = models.CharField(max_length=1000000)

class Revenue(models.Model):
    Revenue_value = models.IntegerField()