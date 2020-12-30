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
                    font_family_name = destination.removeprefix("font_storage/")
                    #Gets path to directory[1]
                    font_family_path = destination

                    try:
                        # Save path to database[2]
                        save_path = FontFamily(path_to_font_family=font_family_path, font_family_name=font_family_name)
                        save_path.save()

                        self.stdout.write(f"✅ Successfully copied {str(font_family_name)} to {dst}")
                    except:
                        self.stdout.write(f"🚨 Error attempting to save {save_path}")

                    # Saving Font
                    for i in os.listdir(font_family_path):
                        if i != ".DS_Store": # During development on macOS there is a .DS_Store file that we do not want to transfer. This check is in place for that reason
                            try:
                                save_font = Font(font_name=i, font_family=save_path)
                                save_font.save()

                                self.stdout.write(f"    👍 Font {i} saved to 📂 {save_path}")
                            except:
                                self.stdout.write(f"🚨 Error check that {i} doesn't already exist in {save_path}")

                except:
                    self.stdout.write(f"🚨 Error because a directory for {font_family_name} already exists")




        #print("-----------------------------")
        #print("Output from create_font_json.py")
        # CURRENT STATUS: Just walks and prints the contents of the font_storage folder after copying the files
        #create_font_json.create_json()
        # Should save to database
