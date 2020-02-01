# files.py
__version__ = "v20200120"

import os
import glob


def file_list(folder):
    # Grabs the PDF's in the requested order
    fileList = sorted(glob.glob("".join([folder, "*.pdf"]))
                      )  # Gathers all the Files
    # Strips the file path data to leave just the filename
    Stripped_List = [os.path.basename(x) for x in fileList]
    return Stripped_List  # Returns the Stripped List to Main Function

