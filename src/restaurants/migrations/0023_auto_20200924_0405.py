# Generated by Django 3.1 on 2020-09-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0022_restaurant_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=80, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nombre de tienda'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr-codes', verbose_name='Código QR'),
        ),
    ]