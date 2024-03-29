# Generated by Django 3.2.9 on 2021-11-25 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donate', '0011_donorextra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemsdonated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngoname', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=400)),
                ('quantity', models.IntegerField(max_length=10)),
                ('pickup', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
