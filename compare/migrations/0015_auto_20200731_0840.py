# Generated by Django 3.0.7 on 2020-07-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0014_ocrupdate_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocrupdate',
            name='currently_parsed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='path',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='tif',
            name='path',
            field=models.TextField(unique=True),
        ),
    ]
