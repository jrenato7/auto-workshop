from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(verbose_name='placa', max_length=10)
    brand = models.CharField(verbose_name='marca', max_length=50)
    model = models.CharField(verbose_name='modelo', max_length=50)
    year = models.IntegerField(verbose_name='ano')
    color = models.CharField(verbose_name='cor', max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " - ".join([self.brand, self.plate])

