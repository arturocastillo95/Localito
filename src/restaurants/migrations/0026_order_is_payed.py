# Generated by Django 3.2.7 on 2021-10-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0025_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_payed',
            field=models.BooleanField(default=False),
        ),
    ]
