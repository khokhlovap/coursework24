# Generated by Django 5.1.2 on 2025-01-14 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("realty", "0024_alter_historicalinfobuilding_updated_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="apartment",
            options={
                "ordering": ["-code_building"],
                "verbose_name": "Апартаменты",
                "verbose_name_plural": "Апартаменты",
            },
        ),
    ]
