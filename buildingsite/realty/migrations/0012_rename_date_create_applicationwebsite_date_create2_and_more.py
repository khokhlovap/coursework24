# Generated by Django 5.1.2 on 2024-11-22 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0011_rename_data_change_statusapartment_data_change2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationwebsite',
            old_name='date_create',
            new_name='date_create2',
        ),
        migrations.RenameField(
            model_name='statusapartment',
            old_name='data_change2',
            new_name='data_change',
        ),
    ]
