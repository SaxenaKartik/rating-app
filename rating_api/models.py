from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    """ Custom user model """
    pass
    def __str__(self):
        return "username : " +str(self.username)
    class Meta :
        verbose_name_plural = "MyUsers"

class Product(models.Model):
    """ Custom product model """
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    rating = models.DecimalField(max_digits = 5, decimal_places = 2)
    def __str__(self):
        return "name : " + str(self.name) + " price : " + str(self.price) + " rating : " + str(self.rating)

class Rate(models.Model):
    """Rate model"""
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    rating = models.DecimalField(max_digits = 5, decimal_places = 2)
