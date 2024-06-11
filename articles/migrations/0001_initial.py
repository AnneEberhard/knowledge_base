# Generated by Django 5.0.6 on 2024-06-11 09:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, unique=True)),
                ('author', models.CharField(default='', max_length=100, unique=True)),
                ('text', models.CharField(default='', max_length=800, unique=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]