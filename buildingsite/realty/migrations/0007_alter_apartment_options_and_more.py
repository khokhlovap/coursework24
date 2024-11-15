# Generated by Django 5.1.2 on 2024-11-07 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0006_applicationwebsite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Апартаменты', 'verbose_name_plural': 'Апартаменты'},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='code_building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.infobuilding', verbose_name='Код здания'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='number_floor',
            field=models.SmallIntegerField(verbose_name='Номер этажа'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='number_rooms',
            field=models.SmallIntegerField(verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=12, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='square',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Площадь, кв.м'),
        ),
    ]
