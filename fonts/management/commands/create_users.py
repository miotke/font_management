"""
USAGE: `python manage.py create_users x`
where x = the name of the account you want to create(one word only)
"""

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create user accounts"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Indicates the number of users to be created")


    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        password = get_random_string()

        User.objects.create_user(username=name, email="", password=password)

        self.stdout.write(f"Account created \n 🙋‍♂️Username: {name} \n 🔐 Password: {password} \n")
