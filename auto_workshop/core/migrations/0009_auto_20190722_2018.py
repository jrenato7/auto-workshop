# Generated by Django 2.2.3 on 2019-07-22 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190718_2035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Labor',
            new_name='OrderLabor',
        ),
        migrations.RenameModel(
            old_name='Part',
            new_name='OrderPart',
        ),
    ]
