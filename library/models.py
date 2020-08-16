from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return ("{} {}".format(self.first_name, self.last_name))

class BookType(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    #type = models.CharField(max_length=200, null=True)
    type = models.ForeignKey(BookType,on_delete=models.SET_NULL, null=True)
    #add_date = models.DateTimeField('Date added',null=True, blank=True)

    def __str__(self):
        return (self.title)
