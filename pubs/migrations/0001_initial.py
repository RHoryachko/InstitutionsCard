# Generated by Django 3.2.23 on 2023-12-21 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, validators=[django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField(blank=True)),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='establishment_photos/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='establishment_photos/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='establishment_photos/')),
                ('category', models.CharField(choices=[('cheap', 'Дешево'), ('medium', 'Середньо'), ('expensive', 'Дорого'), ('very_expensive', 'Дуже дорого')], default='medium', max_length=20)),
            ],
        ),
    ]
