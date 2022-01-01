# Generated by Django 4.0 on 2021-12-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('book_description', models.CharField(max_length=20)),
                ('book_image', models.ImageField(upload_to='book_pics/')),
                ('quantity', models.IntegerField()),
                ('quantity_inlibrary', models.IntegerField(blank=True, null=True)),
                ('quantity_outlibrary', models.IntegerField(blank=True, null=True)),
                ('quantity_indemand', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
