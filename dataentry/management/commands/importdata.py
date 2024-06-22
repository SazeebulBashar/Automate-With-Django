from django.core.management.base import BaseCommand
# from dataentry.models import Student
from django.apps import apps
import csv
# proposed command --> python manage.py importdata file_path model_name

class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help = "The path of the csv file")
        parser .add_argument('model_name', type=str, help = "The name of the model")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name']

        # Search for model in all installed apps
        for app_config in apps.get_app_config():
            # searching for model
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue # model not found in this app, continue searching in next app

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model_name.objects.create(**row)
                
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
        