# Generated by Django 4.2.13 on 2024-07-25 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0002_alter_postings_url_generated"),
    ]

    operations = [
        migrations.CreateModel(
            name="Applications",
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
                ("applicant_name", models.CharField(max_length=250)),
                ("applicant_email", models.CharField(max_length=250)),
                ("resume", models.FileField(upload_to="resumes/")),
                (
                    "job_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registered_job_id",
                        to="users.postings",
                    ),
                ),
            ],
        ),
    ]
