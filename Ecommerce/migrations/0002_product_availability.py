# Generated by Django 5.0.6 on 2024-06-18 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
