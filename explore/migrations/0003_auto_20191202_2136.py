# Generated by Django 2.2.7 on 2019-12-02 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("explore", "0002_auto_20191202_1431"),
    ]

    operations = [
        migrations.RenameField(model_name="corpus", old_name="len", new_name="length",),
    ]
