# Generated by Django 2.2.3 on 2019-07-14 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190710_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantidade')),
                ('description', models.CharField(max_length=255, verbose_name='descrição')),
                ('unity', models.DecimalField(decimal_places=10, max_digits=14, verbose_name='valor unitário')),
                ('amount', models.DecimalField(decimal_places=10, max_digits=14, verbose_name='total')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order', verbose_name='Serviço')),
            ],
            options={
                'verbose_name': 'peça',
                'verbose_name_plural': 'peças',
            },
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('F', 'Reparo'), ('R', 'Substituição')], max_length=1, verbose_name='tipo')),
                ('description', models.CharField(max_length=255, verbose_name='descrição')),
                ('price', models.DecimalField(decimal_places=10, max_digits=14, verbose_name='valor')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order', verbose_name='serviço')),
            ],
            options={
                'verbose_name': 'mão de obra',
                'verbose_name_plural': 'mão de obra',
            },
        ),
    ]