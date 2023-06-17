# Generated by Django 4.1.7 on 2023-06-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_item_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
