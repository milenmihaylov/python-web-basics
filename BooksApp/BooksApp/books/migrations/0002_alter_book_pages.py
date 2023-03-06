# Generated by Django 4.1.7 on 2023-03-04 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0)]),
        ),
    ]
