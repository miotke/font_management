import os
import json
import requests


# Web request
ENDPOINT = "font-family"
ID = 24 # ID is the int in the URL. We need to find a way to change this int to list all fonts
URL = f"http://127.0.0.1:8000/{ENDPOINT}/{ID}/" #change this to the actual server address
HEADER = {
    "Content-Type": "application/json"
}


font_list = []
BANNER = """
 ********   *******   ****     ** **********  ********
/**/////   **/////** /**/**   /**/////**///  **//////
/**       **     //**/**//**  /**    /**    /**
/******* /**      /**/** //** /**    /**    /*********
/**////  /**      /**/**  //**/**    /**    ////////**
/**      //**     ** /**   //****    /**           /**
/**       //*******  /**    //***    /**     ********
//         ///////   //      ///     //     ////////

A simple command line version of a font manager.
"""


def list_fonts():
    # 1. Make a request to api and return json
    response = requests.get(URL, headers=HEADER)
    json_data = response.json()

    # 2. Loop through json
    for (key, value) in json_data.items():
        # 3. Get the font family
        if key == "font_family_name":
            font_family = value
            print(f"{font_family}")
        # 4. Get the fonts for a font family
        if key == "fonts":
            fonts = value
            for font in fonts:
                print(f"    {font}")
                font_list.append(font)

    return font_list


if __name__ == "__main__":
    print(BANNER)
    list_fonts()
