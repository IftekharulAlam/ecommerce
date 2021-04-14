from django.db import models

# Create your models here.
class shopData(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price=models.IntegerField()
    img = models.ImageField(upload_to='images')