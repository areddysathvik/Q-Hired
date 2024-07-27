# Generated by Django 4.2.13 on 2024-07-26 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0005_remove_postings_url_generated_postings_date_posted"),
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
