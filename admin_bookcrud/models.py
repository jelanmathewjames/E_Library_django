from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=20)
    book_description = models.CharField(max_length=20)
    book_image = models.ImageField(upload_to='book_pics/')