# Generated by Django 5.1.2 on 2024-11-22 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0014_applicationwebsite_date_create4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationwebsite',
            name='date_create2',
        ),
        migrations.RemoveField(
            model_name='applicationwebsite',
            name='date_create4',
        ),
    ]
