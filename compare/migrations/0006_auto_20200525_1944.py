# Generated by Django 3.0.6 on 2020-05-25 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0005_auto_20200525_1902'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ocrupdate',
            unique_together={('slug', 'timestamp', 'pdf')},
        ),
    ]