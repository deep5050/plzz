import json
import os
import requests

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __upload_to_gist(
    file_path: str, gist_description: str, is_public: bool, github_token: str
) -> str:
    # Read the contents of the file
    with open(file_path, "r") as file:
        file_contents = file.read()

    # Construct the Gist payload
    payload = {
        "description": gist_description,
        "public": is_public,
        "files": {os.path.basename(file_path): {"content": file_contents}},
    }

    # Set the authentication headers
    headers = {"Authorization": f"Bearer {github_token}"}
    try:
        # Make the HTTP POST request to create the Gist
        response = requests.post(
            "https://api.github.com/gists", json=payload, headers=headers
        )
        # print(response.status_code)
        # Check the response status code
        if response.status_code != 201:
            print(
                "{}{}ERROR: Filed to upload '{}'{}!".format(
                    colors.BOLD, colors.FAIL, file_path, colors.ENDC
                )
            )
            return ""
    except:
        print(
            "{}{}ERROR: Something went wrong during upload '{}'{}!".format(
                colors.BOLD, colors.FAIL, file_path, colors.ENDC
            )
        )
        return ""

    # Return the Gist URL
    return json.loads(response.text)["html_url"]


def upload_to_gist_smartly(pathname: str, mode: str, description: str = ""):
    """Upload a file or all files under a directory to Github Gist.

    Args:
        pathname (str): Path to a file or a directory.
        mode (str): public or private.
        description (str): short description for the gist.
    """
    # validate mode
    if mode == "public":
        public = True
    elif mode == "private":
        public = False
    else:
        print(
            "{}{}ERROR: Please specify a mode (public/private).{}".format(
                colors.BOLD, colors.FAIL, colors.ENDC
            )
        )
        return

    # get token from home directory
    token_file_name = ".gist_token"
    token_path = os.path.join(os.path.expanduser("~"), token_file_name)
    if not os.path.exists(token_path):
        print(
            "{}{}ERROR: Please create a file '{}' nuder your home directory with your API token!{}".format(
                colors.BOLD, colors.FAIL, token_path, colors.ENDC
            )
        )
        return
    with open(token_path, "r") as f:
        token = f.read()
        token = token.strip()

    if token == "":
        print(
            "{}{}ERROR: Please write the API key into '{}'!{}".format(
                colors.BOLD, colors.FAIL, token_file_name, colors.ENDC
            )
        )
        return

    files = __pathname_checker(pathname)

    for filename in files:
        return_url = __upload_to_gist(filename, description, public, token)
        if not return_url == "":
            print(
                "{}{}GIST: File '{}' -> '{}' {}".format(
                    colors.BOLD, colors.OKGREEN, filename, return_url, colors.ENDC
                )
            )
