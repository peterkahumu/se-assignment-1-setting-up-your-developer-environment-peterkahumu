# Generated by Django 5.0.6 on 2024-07-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0005_remove_product_image_product_imagge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imagge',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no image uploaded', upload_to='products/'),
        ),
    ]
