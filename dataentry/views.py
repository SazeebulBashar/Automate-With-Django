from django.shortcuts import render
from . utils import get_all_custom_model
from uploads.models import Upload
from django.shortcuts import redirect
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages

# Create your views here.

def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')

        # store the file path and model name in the database
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        
        # construct the full path of the uploaded file
        relative_path = str(upload.file.url)
        base_path = str(settings.BASE_DIR)

        file_path = base_path + relative_path
        # print(file_path)

        # trigger the command to import the data
        try:
            call_command('importdata', file_path, model_name)
            messages.success(request, 'Data imported successfully')
        except Exception as e:
            messages.error(request, str(e))
            

        return redirect('import_data')
    else:
        models = get_all_custom_model()
        context = {
            'models': models
        }
    return render(request, 'dataentry/importdata.html', context)
