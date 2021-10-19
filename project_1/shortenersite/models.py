from django.db import models


class Url(models.Model):
    long_url = models.CharField(max_length=10000)
    token = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
