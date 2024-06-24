from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
from django.db import DataError
# proposed command --> python manage.py importdata <file_path> <model_name>

class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help = "The path of the csv file")
        parser.add_argument('model_name', type=str, help = "The name of the model")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # Search for model in all installed apps
        model =None
        for app_config in apps.get_app_configs():
            # searching for model
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue # model not found in this app, continue searching in next app

        if not model:
            raise CommandError(f"Model '{model_name}' was not found.")
        
        model_fields = [field.name for field in model._meta.get_fields() if field.name != 'id']


        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            csv_header = reader.fieldnames
            if csv_header != model_fields:
                raise DataError("CSV headers doesn't match model fields.")
            for row in reader:
                model.objects.create(**row)
                
        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
        