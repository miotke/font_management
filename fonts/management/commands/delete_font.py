"""
This command takes a font family name that already exists in the font_storage
directory and removes it along with all files within that directory.

The command already assumes the entire path except for the font family group name
that needs to be passed in. This is currently font_storage/ but will need to be repalced
with whatever would be used as the file storage, i.e. AWS S3

USAGE: python manage.py delete_font [name of font group]
"""

import os
import shutil
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command takes a font family name that already exists in the font_storage directory and removes it along with all files within that directory."

    def add_arguments(self, parser):
        parser.add_argument("font_family", type=str, help="Removes the font family group that is passed in.")


    def handle(self, *args, **kwargs):
        path = "font_storage"
        font_family_to_remove = kwargs["font_family"]
        font_path = os.path.join(path, font_family_to_remove)

        try:
            shutil.rmtree(font_path)
            self.stdout.write(f"✅ Successfully removed {font_path}")

        except OSError as e:
            self.stdout.write(f"🚨Error {font_path} : {e.strerror}")
