# Generated by Django 5.0.6 on 2024-06-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(default='', max_length=5000, unique=True),
        ),
    ]
