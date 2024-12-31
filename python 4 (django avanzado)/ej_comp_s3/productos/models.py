from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL, blank=True, null=True)
