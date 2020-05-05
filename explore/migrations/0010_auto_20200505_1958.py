# Generated by Django 3.0.6 on 2020-05-05 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("explore", "0009_auto_20200420_1521"),
    ]

    operations = [
        migrations.AlterField(
            model_name="corpus",
            name="language",
            field=models.ForeignKey(
                choices=[
                    ("benepar_ar", "ar"),
                    ("benepar_de", "de"),
                    ("benepar_en_small", "en"),
                    ("benepar_eu", "eu"),
                    ("benepar_fr", "fr"),
                    ("benepar_he", "he"),
                    ("benepar_hu", "hu"),
                    ("benepar_ko", "ko"),
                    ("benepar_pl", "pl"),
                    ("benepar_sv", "sv"),
                    ("benepar_zh", "zh"),
                ],
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="explore.Language",
            ),
        ),
    ]