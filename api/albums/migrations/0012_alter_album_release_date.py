# Generated by Django 5.1.1 on 2024-10-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0011_alter_record_album"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="release_date",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
