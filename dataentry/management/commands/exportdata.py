from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import csv
from django.apps import apps

# proposed command --> python manage.py exportdata <file_path> <model_name>

class Command(BaseCommand):
    help = 'Export data to csv file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help = "The name of the model")

    def handle(self, *args, **kwargs):
        # file_path = kwargs['file_path']
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

        # Fetch the data from the database
        data = model.objects.all()

        # Generate the timestamp for the file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        #  Define the csv file name
        file_path = f'data_export_{timestamp}.csv'

        # open the csv file and Write the data to a CSV file
        with open(f'data_export_{timestamp}.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow([field.name for field in model._meta.fields])
            
            # Write the data rows from 2 to end
            for row in data:
                writer.writerow([getattr(row, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS(f"Data exported successfully to {file_path}"))