# Generated by Django 3.2.9 on 2021-11-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Donate', '0002_delete_ngolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ngolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngoname', models.CharField(max_length=150)),
                ('year_founded', models.IntegerField()),
                ('offwebsite', models.CharField(max_length=100)),
                ('mobno', models.CharField(max_length=10)),
                ('ngo_email', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
    ]
