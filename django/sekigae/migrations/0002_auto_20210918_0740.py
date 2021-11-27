# Generated by Django 3.2.7 on 2021-09-17 22:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sekigae", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SeatSheet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created_at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated_at")),
                ("name", models.CharField(max_length=255)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                (
                    "student_sheet",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sekigae.studentsheet"),
                ),
            ],
            options={
                "verbose_name": "seat_sheet",
                "verbose_name_plural": "seat_sheets",
            },
        ),
        migrations.CreateModel(
            name="SeatPair",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created_at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated_at")),
                ("seat", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sekigae.seat")),
                ("seat_sheet", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sekigae.seatsheet")),
                ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sekigae.student")),
            ],
            options={
                "verbose_name": "seat_pair",
                "verbose_name_plural": "seat_pairs",
            },
        ),
        migrations.AddConstraint(
            model_name="seatsheet",
            constraint=models.UniqueConstraint(fields=("name", "owner_id"), name="seat_sheet_unique"),
        ),
    ]