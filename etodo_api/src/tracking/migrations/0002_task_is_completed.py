# Generated by Django 4.2.3 on 2023-07-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracking", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False, verbose_name="is closed"),
        ),
    ]
