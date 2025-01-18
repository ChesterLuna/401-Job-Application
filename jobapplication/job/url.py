from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # This maps the URL to the job_list view
]