# Generated by Django 3.1 on 2020-09-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0021_auto_20200902_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr-codes', verbose_name='Código QR'),
        ),
    ]
