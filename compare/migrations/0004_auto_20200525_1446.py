# Generated by Django 3.0.6 on 2020-05-25 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("compare", "0003_pdf"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="pdf", unique_together={("slug", "num")},),
    ]
