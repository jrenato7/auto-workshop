# Generated by Django 2.2.3 on 2019-07-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190705_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='marca'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(max_length=15, verbose_name='cor'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=50, verbose_name='modelo'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate',
            field=models.CharField(max_length=10, verbose_name='placa'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(verbose_name='ano'),
        ),
    ]
