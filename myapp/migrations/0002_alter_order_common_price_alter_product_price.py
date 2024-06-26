# Generated by Django 5.0.6 on 2024-06-26 11:53

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='common_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[myapp.models.validate_not_negative]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[myapp.models.validate_not_negative]),
        ),
    ]