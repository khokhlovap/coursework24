# Generated by Django 5.1.2 on 2024-11-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0013_applicationwebsite_date_create3'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationwebsite',
            name='date_create4',
            field=models.DateField(blank=True, null=True, verbose_name='Дата изменения статуса'),
        ),
    ]
