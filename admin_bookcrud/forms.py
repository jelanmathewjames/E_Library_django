from django import forms
from . models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('book_name',
                  'book_category',
                  'book_author',
                  'book_price',
                  'book_image')