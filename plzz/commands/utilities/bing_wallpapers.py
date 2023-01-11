import requests
import os
from datetime import datetime


from plzz.helper_functions.helper_functions import colors

def download_bing_wallpaper(directory:str):
    """Download today's wallpaper from bing, and save them.

    Args:
        directory (str): Path to the directory.
    """
    if not os.path.isdir(directory):
        print("{}{}ERROR: directory '{}' does not exist!".format(
            colors.BOLD,
            colors.FAIL,
            directory,
            colors.ENDC
        ))
        return
    # Get the current date
    today = datetime.today().strftime("%d-%m-%Y")

    try:
        # Get the URL of the Bing wallpaper of the day
        url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        response = requests.get(url)
        data = response.json()
        image_url = f"https://www.bing.com{data['images'][0]['url']}"

        # Download the wallpaper
        response = requests.get(image_url)
        image_path = os.path.join(directory, f"{today}.jpg")
    
        open(image_path, "wb").write(response.content)
        print("{}{}DOWNLOADED:  '{}' is today's wallpaper!{}".format(
            colors.BOLD,
            colors.OKGREEN,
            image_path,
            colors.ENDC
        ))
    except:
        print("{}{}ERROR: Something went wrong downloading today's wallpaper!{}".format(
            colors.BOLD,
            colors.FAIL,
            colors.ENDC
        ))

