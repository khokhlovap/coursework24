# Generated by Django 5.1.2 on 2024-11-22 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0010_applicationwebsite_date_create_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusapartment',
            old_name='data_change',
            new_name='data_change2',
        ),
    ]
