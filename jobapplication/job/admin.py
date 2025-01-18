# job/admin.py
from django.contrib import admin

# Import the models here, where they are used
def register_models():
    from .models import Job, JobApplication
    admin.site.register(Job)
    admin.site.register(JobApplication)

register_models()


# Register your models here.
