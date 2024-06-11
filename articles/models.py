from django.utils import timezone
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, default='')
    author = models.CharField(max_length=100, unique=True, default='')
    text = models.CharField(max_length=5000, unique=True, default='')
    created_at = models.DateField(default=timezone.now)