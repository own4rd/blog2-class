from django.db import models
from .category import Category


class Post(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
