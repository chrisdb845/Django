from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity= models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    description= models.TextField()


    def __str__(self):
        return self .name
