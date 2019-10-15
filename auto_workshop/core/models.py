# -*- coding: utf-8 -*-
from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(verbose_name='placa', max_length=10)
    brand = models.CharField(verbose_name='marca', max_length=50)
    model = models.CharField(verbose_name='modelo', max_length=50,
                             blank=True, null=True)
    year = models.IntegerField(verbose_name='ano', blank=True, null=True)
    color = models.CharField(verbose_name='cor', max_length=15,
                             blank=True, null=True)
    odometer = models.IntegerField(verbose_name='quilometragem', null=True,
                                   blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " - ".join([self.brand, self.plate])

    def save(self, *args, **kwargs):
        self.plate = self.plate.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'


class Order(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE,
                                verbose_name='veículo')
    date = models.DateField(verbose_name='data do serviço')
    odometer = models.IntegerField(verbose_name='quilometragem',
                                   null=True, blank=True)

    def __str__(self):
        return str(self.vehicle)

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'


class OrderPart(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE,
                              verbose_name='Serviço')
    quantity = models.IntegerField(verbose_name='quantidade')
    description = models.CharField(verbose_name='descrição', max_length=255)
    unity = models.DecimalField(verbose_name='valor unitário',
                                decimal_places=2,
                                max_digits=14)
    amount = models.DecimalField(verbose_name='total',
                                 decimal_places=2,
                                 max_digits=14)

    class Meta:
        verbose_name = 'peça'
        verbose_name_plural = 'peças'

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.unity
        super().save(*args, **kwargs)


class OrderLabor(models.Model):
    FIX = 'F'
    REPLACE = 'R'
    KINDS = (
        (FIX, 'Reparo'),
        (REPLACE, 'Substituição')
    )
    order = models.ForeignKey('Order', on_delete=models.CASCADE,
                              verbose_name='serviço')
    kind = models.CharField(verbose_name='tipo', max_length=1, choices=KINDS)
    description = models.CharField(verbose_name='descrição', max_length=255)
    price = models.DecimalField(verbose_name='valor',
                                decimal_places=2,
                                max_digits=14)

    class Meta:
        verbose_name = 'mão de obra'
        verbose_name_plural = 'mão de obra'
