from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def job(request):
    return render(request, "index.html")

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # Do something with the uploaded file
        return render(request, 'upload_success.html', {'file_name': uploaded_file.name})
    else:
        return render(request, 'upload_file.html')