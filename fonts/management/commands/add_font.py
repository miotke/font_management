"""
This management command takes a directory of font files(.ost) and copies them
to the font_storage directory.

USAGE: python manange.py add_font [path_to_folder_of_fonts]
"""

import os
import json
import shutil
from fonts.models import Font
from fonts.models import FontFamily
from helper_scripts import create_font_json
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = """Takes a directory of fonts and uploads them to font_storage.\n
    The base directory that is taken in should be the font_family with
    only the font files(.otf file type) being inside the directory.
    """


    def add_arguments(self, parser):
        parser.add_argument("font_family_folder", type=str, help="Pass in a directory of fonts to upload to the font server.")


    def handle(self, *args, **kwargs):
        src = kwargs["font_family_folder"]
        dst = "font_storage/"
        symlinks = False
        ignore = None

        for item in os.listdir(src):
            source = os.path.join(src, item)
            destination = os.path.join(dst, item)
            if os.path.isdir(source):
                """
                1. Get path to directory
                2. Save the path to the directory in the database
                """
                try:
                    shutil.copytree(source, destination, symlinks, ignore)
                    #Gets path to directory[1]
                    font_family_path = destination
                    # Save path to database[2]
                    save_path = FontFamily(path_to_font_family=font_family_path)
                    save_path.save()

                except:
                    self.stdout.write(f"Error because the directory {destination} already exists")




        #print("-----------------------------")
        #print("Output from create_font_json.py")
        # CURRENT STATUS: Just walks and prints the contents of the font_storage folder after copying the files
        #create_font_json.create_json()
        # Should save to database
