from django.shortcuts import render

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # Do something with the uploaded file
        return render(request, 'upload_success.html', {'file_name': uploaded_file.name})
    else:
        return render(request, 'upload_file.html')
