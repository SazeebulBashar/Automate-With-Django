from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "greets the users."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help = "The name of the person to greet")


    def handle(self,*args,  **kwargs):
        name = kwargs['name']
        msg = f'Hello {name}!. Welcome to django Command Management, Boss.'
        self.stdout.write(self.style.SUCCESS(msg))