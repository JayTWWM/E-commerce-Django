from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=120,unique=True)
    seller      = models.TextField()
    picLink     = models.URLField(max_length=700)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=10000)
    discount    = models.DecimalField(decimal_places=2,max_digits=4)
    active      = models.BooleanField(default=True)
    discounted  = models.BooleanField(default=False)
    date        = models.DateField(null=True)