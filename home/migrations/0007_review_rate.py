# Generated by Django 5.1.2 on 2024-11-01 14:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'eng kam baho 1'), django.core.validators.MaxValueValidator(5, "eng ko'p baho 5")]),
            preserve_default=False,
        ),
    ]
