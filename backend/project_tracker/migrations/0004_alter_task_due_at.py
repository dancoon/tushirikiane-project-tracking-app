# Generated by Django 5.0 on 2024-02-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_tracker", "0003_alter_request_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="due at"),
        ),
    ]
