# Generated by Django 4.2.10 on 2024-03-18 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_products_image2_products_image3_products_image4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, unique=True),
        ),
    ]
