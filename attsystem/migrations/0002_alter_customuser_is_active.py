# Generated by Django 5.0.6 on 2024-07-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attsystem", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
