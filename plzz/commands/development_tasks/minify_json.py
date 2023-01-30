import json
import os

from plzz.helper_functions.snippets import __pathname_checker
from plzz.helper_functions.helper_functions import colors


def __minify_json_file(json_file_path) -> None:

    # Read the JSON file
    try:
        with open(json_file_path, "r") as file:
            json_text = file.read()

        # Parse the JSON text
        data = json.loads(json_text)

        # Minify the JSON text
        json_text = json.dumps(data, separators=(",", ":"))

        # Write the minified JSON text back to the file
        with open(json_file_path, "w") as file:
            file.write(json_text)
        print(
            "{}{}MINIFIED: '{}' minified successfully".format(
                colors.BOLD, colors.OKGREEN, json_file_path, colors.ENDC
            )
        )
    except:
        print("{}{}ERROR: Something went wrong during minifying '{}'{}".format(
            colors.BOLD,
            colors.FAIL,
            json_file_path,
            colors.ENDC
        ))


def minify_json_files(pathname: str):
    """Minify JSON files.

    Args:
        pathname (str): Path to a JSON file or path to a directory.
    """
    filepaths = __pathname_checker(pathname)

    for filepath in filepaths:
        _, ext = os.path.splitext(filepath)
        if not ext == ".json":
            print(
                "{}{}ERROR: '{}' is not a JSON file!{}".format(
                    colors.BOLD, colors.FAIL, filepath, colors.ENDC
                )
            )
        else:
            __minify_json_file(filepath)
