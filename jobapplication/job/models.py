# job/models.py
from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()

    def __str__(self):
        return self.job_title

# You can import JobApplicationAdmin only where it is needed
def some_function():
    from job.admin import JobApplicationAdmin
    # Use JobApplicationAdmin as needed
