# Generated by Django 3.2.7 on 2021-11-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngolist',
            name='mobno',
            field=models.CharField(max_length=10),
        ),
    ]
