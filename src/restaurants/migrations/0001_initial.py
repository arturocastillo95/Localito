# Generated by Django 3.1 on 2020-08-19 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=80)),
                ('city', models.CharField(blank=True, max_length=60)),
                ('country', models.CharField(blank=True, max_length=60)),
                ('postal_code', models.CharField(blank=True, max_length=60)),
                ('image', models.ImageField(default='default/logo-restaurant-default.jpg', upload_to='restaurant-images', verbose_name='Logo de Restaurante')),
                ('about', models.TextField(blank=True, max_length=300)),
                ('whatsapp_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('facebook_url', models.URLField(blank=True, max_length=60, verbose_name='Link de Facebook')),
                ('instagram_url', models.URLField(blank=True, max_length=60, verbose_name='Link de Instagram')),
                ('owner', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('order', models.IntegerField(blank=True)),
                ('restaurant', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True, max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('section', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurants.section')),
            ],
        ),
    ]
