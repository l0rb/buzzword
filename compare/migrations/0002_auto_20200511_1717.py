# Generated by Django 3.0.6 on 2020-05-11 17:17

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ("compare", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", martor.models.MartorField()),
                ("wiki", martor.models.MartorField()),
            ],
        ),
        migrations.DeleteModel(name="OCRText",),
    ]
