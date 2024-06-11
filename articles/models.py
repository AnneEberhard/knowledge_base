from django.utils import timezone
from django.db import models

class Article(models.Model):
    """
    Model für einen Artikel in der Knowledge Base.

    Attributes:
        title (str): Der Titel des Artikels.
        author (str): Der Autor des Artikels.
        text (str): Der Text des Artikels.
        created_at (Date): Das Datum, an dem der Artikel erstellt wurde.
    """
    title = models.CharField(max_length=100, unique=True, default='')
    author = models.CharField(max_length=100, unique=True, default='')
    text = models.CharField(max_length=5000, unique=True, default='')
    created_at = models.DateField(default=timezone.now)