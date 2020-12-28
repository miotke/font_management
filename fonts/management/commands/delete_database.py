import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = """
    --- DEV HELPER COMMAND ONLY ---
    DO NOT USE THIS COMMAND ONT HE PROD SERVER.
    This deletes the databse(db.sqlite3) and the fonts/migrations folder contents.
    """

    def handle(self, *args, **kwargs):
        os.system("rm -r db.sqlite3")
        os.system("rm -r fonts/migrations/0*")

        self.stdout.write("Removed database")
        self.stdout.write("Removed migrations")
