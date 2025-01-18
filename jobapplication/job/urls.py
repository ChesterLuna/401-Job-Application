from django.urls import path
from . import views

urlpatterns = [
    path("", views.job, name="job"),
    path('upload/', views.upload_file, name='upload_file'),
]