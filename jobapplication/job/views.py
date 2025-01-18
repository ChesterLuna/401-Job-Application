from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()  # Fetch all jobs from the database
    return render(request, 'job/job_list.html', {'jobs': jobs})
