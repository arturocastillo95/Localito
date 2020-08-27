# Generated by Django 3.1 on 2020-08-19 20:44

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, upload_to='restaurant-images', verbose_name='Logo de Restaurante'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='whatsapp_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
