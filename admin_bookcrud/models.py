from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=20)
    book_description = models.CharField(max_length=20)
    book_image = models.ImageField(upload_to='book_pics/')
    book_price = models.FloatField(max_length=20)
    book_inhand = models.BooleanField(default=False)
    book_author = models.CharField(max_length=20)