from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = 'Inserts data into the database'

    def handle(self, *args,  **kwargs):
        # add 1 data
        # Student.objects.create(roll_no="1", name = "Sazeebul Bashar", age=24)

        # add multiple data
        dataset = [
            {'roll_no': '1', 'name': 'Sanjana Bashar', 'age': 24},
            {'roll_no': '2', 'name': 'Sazeebul Bashar', 'age': 24},
            {'roll_no': '3', 'name': 'Shah Rukh Khan', 'age': 54},
            {'roll_no': '4', 'name': 'Salman Khan', 'age': 44},
            {'roll_no': '5', 'name': 'Akshay Kumar', 'age': 49},
            {'roll_no': '6', 'name': 'Aamir Khan', 'age': 56},
            {'roll_no': '7', 'name': 'Anushka Sharma', 'age': 34},
            {'roll_no': '8', 'name': 'Shahid Kapoor', 'age': 24},
            {'roll_no': '9', 'name': 'Salman Khan', 'age': 44},
            {'roll_no': '10', 'name': 'Akshay Kumar', 'age': 49},
            {'roll_no': '11', 'name': 'Aamir Khan', 'age': 56},
            {'roll_no': '12', 'name': 'Anushka Sharma', 'age': 34},
            {'roll_no': '13', 'name': 'Shahid Kapoor', 'age': 24},
            {'roll_no': '14', 'name': 'Salman Khan', 'age': 44},
            {'roll_no': '15', 'name': 'Akshay Kumar', 'age': 49},
            {'roll_no': '16', 'name': 'Aamir Khan', 'age': 56},
            {'roll_no': '17', 'name': 'Anushka Sharma', 'age': 34},
            {'roll_no': '18', 'name': 'Shahid Kapoor', 'age': 24},
            {'roll_no': '19', 'name': 'Salman Khan', 'age': 44},
            {'roll_no': '20', 'name': 'Akshay Kumar', 'age': 49},
            {'roll_no': '21', 'name': 'Aamir Khan', 'age': 56},
            {'roll_no': '22', 'name': 'Anushka Sharma', 'age': 34},
            {'roll_no': '23', 'name': 'Shahid Kapoor', 'age': 24},
            {'roll_no': '24', 'name': 'Salman Khan', 'age': 44},
            {'roll_no': '25', 'name': 'Akshay Kumar', 'age': 49},
            {'roll_no': '26', 'name': 'Aamir Khan', 'age': 56},
            {'roll_no': '27', 'name': 'Anushka Sharma', 'age': 34},
            {'roll_no': '28', 'name': 'Shahid Kapoor', 'age': 24},
            {'roll_no': '29', 'name': 'Salman Khan', 'age': 44},
            {'roll_no': '30', 'name': 'Akshay Kumar', 'age': 49},
        ]

        for data in dataset:
            record_exist = Student.objects.filter(roll_no=data['roll_no']).exists()
            if not record_exist:
                Student.objects.create(**data)
            else:
                self.stdout.write(self.style.ERROR(f"{data['roll_no'], data['name']} -- record already exist"))
