# Generated by Django 5.1.2 on 2024-10-31 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nomi')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Category-photos/')),
            ],
            options={
                'verbose_name': 'Toifa',
                'verbose_name_plural': 'Toifalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nomi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='narxi')),
                ('is_available', models.BooleanField(verbose_name='bormi')),
                ('size', models.PositiveIntegerField(verbose_name='olchami')),
                ('description', models.TextField(verbose_name='xaqida')),
                ('card_details', models.TextField(verbose_name='card-details')),
                ('shipping', models.TextField(verbose_name='shipping')),
            ],
            options={
                'verbose_name': 'Maxsulot',
                'verbose_name_plural': 'Maxsulotlar',
            },
        ),
    ]
