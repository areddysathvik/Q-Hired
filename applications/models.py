from django.db import models
from users.models import Postings

class Applications(models.Model):
    applicant_id = models.AutoField(primary_key=True)
    applicant_name = models.CharField(max_length=250)
    job_id = models.ForeignKey(Postings, on_delete=models.CASCADE, related_name='registered_job_id')
    applicant_email = models.CharField(max_length=250)
    resume = models.FileField(upload_to='resumes/', blank=False, null=False)

    def __str__(self):
        return f"{self.applicant_name} :::: for JOB id of {self.job_id.job_id}"