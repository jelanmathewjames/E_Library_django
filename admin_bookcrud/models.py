from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=20)
    book_description = models.CharField(max_length=20)
    book_image = models.ImageField(upload_to='book_pics/')
    book_price = models.FloatField(max_length=20)
    book_inhand = models.BooleanField(default=False)
    book_inhandid = models.IntegerField(null=True,blank=True) 
    book_barcode = models.CharField(max_length=40)
    book_category = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)

 