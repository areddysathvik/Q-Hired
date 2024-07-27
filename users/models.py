from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from django.conf import settings

class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=50, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Changed from 'user_set'
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Changed from 'user_set'
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

class Postings(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_jobs')
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=500)
    job_description = models.CharField(max_length=500)
    min_match_rate_req = models.IntegerField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Job ID: {self.job_id} - [{self.job_title}]"
