from django.shortcuts import render
from . utils import get_all_custom_model
# Create your views here.

def import_data(request):
    if request.method == 'POST':
        pass
    else:
        models = get_all_custom_model()
        context = {
            'models': models
        }
    return render(request, 'dataentry/importdata.html', context)
