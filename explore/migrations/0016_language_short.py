# Generated by Django 3.0.5 on 2020-05-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0015_auto_20200531_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='short',
            field=models.CharField(default='en', max_length=10),
            preserve_default=False,
        ),
    ]
