# Generated by Django 3.2.9 on 2021-11-24 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donate', '0010_rename_contact_ngoextra_mail_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donorextra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobno', models.CharField(max_length=10)),
                ('telephone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('mail_id', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
