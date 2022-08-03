from unicodedata import name
from django.db import models

class ShortUrl(models.Model):
    mainUrl = models.CharField(max_length=3500)
    shortUrl = models.CharField(max_length=20)
    def __str__(self):
        return self.mainUrl
