# Generated by Django 3.2.7 on 2021-11-26 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donate', '0017_alter_itemsdonated_ngoname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsdonated',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
