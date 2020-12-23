"""
This management command takes a directory of font files(.ost) and copies them
to the font_storage directory. 

USAGE: python manange.py add_font path_to_folder_of_fonts
"""

import os
import json
import shutil
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
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else: 
                # General execution path
                try:
                    shutil.copy2(s, d)
                    self.stdout.write(f"✅ {item} copied to {d}")
                except Exception: 
                    self.stdout.write(f"🚫 Failed to copy {item} to {d}")
       
        print("-----------------------------")
        # CURRENT STATUS: Just walks and prints the contents of the font_storage folder after copying the files
        create_font_json.create_json()
       
