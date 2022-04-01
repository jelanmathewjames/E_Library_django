from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField()
