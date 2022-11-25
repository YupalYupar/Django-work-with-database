from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=250, unique=True)
