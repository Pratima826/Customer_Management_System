from django.db import models


# Create your models here.
class Customer(models.Model):
         name=models.CharField(max_length=40)
         address=models.CharField(max_length=40)
         age=models.IntegerField()
         mobileno=models.CharField(max_length=15)
         def __str__(self):
                 return self.name

