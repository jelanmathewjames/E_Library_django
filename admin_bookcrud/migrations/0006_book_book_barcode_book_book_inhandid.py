# Generated by Django 4.0.3 on 2022-04-02 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_bookcrud', '0005_book_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_barcode',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_inhandid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
