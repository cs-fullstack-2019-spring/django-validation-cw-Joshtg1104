from django.db import models


# Create your models here.

class CarModel(models.Model):
    make = models.CharField(max_length=60, default="")
    model = models.CharField(max_length=60, default="")
    year = models.IntegerField(max_length=4, default="")
    mpg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.make
