from django.db import models
from django.utils import timezone
# Create your models here.

class MenuType(models.Model):
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=500,null=True, blank=True)

    def __str__(self):
        return self.name

class Menu (models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200,null=True, blank=True)
    photo = models.CharField(max_length=500,null=True, blank=True)
    type = models.ForeignKey(MenuType,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
