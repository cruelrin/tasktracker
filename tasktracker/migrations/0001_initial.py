# Generated by Django 5.0.3 on 2024-03-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("low", "Низкий"),
                            ("medium", "Средний"),
                            ("high", "Высокий"),
                        ],
                        default="medium",
                        max_length=10,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "Новая"),
                            ("in_progress", "В прогрессе"),
                            ("done", "Выполнено"),
                            ("canceled", "Отменено"),
                            ("postponed", "Отложено"),
                        ],
                        default="new",
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
