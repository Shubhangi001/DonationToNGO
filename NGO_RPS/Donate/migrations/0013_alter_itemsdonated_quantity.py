# Generated by Django 3.2.9 on 2021-11-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donate', '0012_itemsdonated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsdonated',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
