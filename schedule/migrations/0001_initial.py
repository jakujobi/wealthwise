# Generated by Django 5.1.6 on 2025-03-11 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0004_alter_profile_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consultation",
            fields=[
                (
                    "consultation_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("scheduled_date", models.DateTimeField()),
                ("status", models.CharField(blank=True, max_length=20, null=True)),
                ("client_rating", models.IntegerField(blank=True, null=True)),
                ("session_notes", models.TextField(blank=True, null=True)),
                (
                    "advisor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.advisor"
                    ),
                ),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client",
                        to="users.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("event_id", models.AutoField(primary_key=True, serialize=False)),
                ("registration_date", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("event_start_time", models.TimeField()),
                ("event_end_time", models.TimeField()),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("event_type", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "organizer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organizer",
                        to="users.profile",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
            ],
        ),
    ]
