# Generated by Django 2.2.3 on 2019-07-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate',
            field=models.CharField(max_length=10),
        ),
    ]