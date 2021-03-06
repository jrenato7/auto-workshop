# Generated by Django 2.2.3 on 2019-07-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.TextField(max_length=10)),
                ('brand', models.TextField(max_length=50)),
                ('model', models.TextField(max_length=50)),
                ('year', models.IntegerField()),
                ('color', models.TextField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
