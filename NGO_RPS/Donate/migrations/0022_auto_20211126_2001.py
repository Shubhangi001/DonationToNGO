# Generated by Django 3.2.7 on 2021-11-26 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donate', '0021_auto_20211126_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsdonated',
            name='ngoname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Donate.ngoextra'),
        ),
        migrations.AlterField(
            model_name='itemsdonated',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
