"""
The purpose of this script will be to monitor the "font_storage"
directory and build the json object from that.

Example:
font_storage
|
|__font_family #This is a folder named after the font family
   |
   |__font_file.ost #This contains all of the font files associated with a "font family"

------------------------------------------------------------------------------------------
TODO:
    - Give this script a better name
"""

import os
import json


def create_json():
    """
    Walks the font_storage folder and prints out the paths
    TODO:
    - Turn the output into proper json as in the example above
    """
    #--TEST CODE--
    for path, subdirs, files in os.walk("font_storage"):
        for name in files:
            font_path = os.path.join(path, name)
            print(font_path)

if __name__ == "__main__":
    create_json()

