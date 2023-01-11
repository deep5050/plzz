import re
import os

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __capitalize_first_character_of_sentence(text):
    try:
        sentences = re.split(r"(?<=[.!?])\s", text)
        capitalized_sentences = [sentence.capitalize() for sentence in sentences]
        return 0, " ".join(capitalized_sentences)
    except:
        return 1, "N/A"


def format_sentences_smartly(pathname: str):
    """Format each sentences correctly in a english text a file or all files under a directory.

    Args:
        pathname (str): Path to a file or a directory.
    """

    files = __pathname_checker(pathname)
    count = 0
    # parse only text files
    for filename in files:
        _, ext = os.path.splitext(filename)
        if not ".txt" == ext:
            print(
                "{}{}ERROR: '{}' is not a text file! {}".format(
                    colors.BOLD, colors.FAIL, filename, colors.ENDC
                )
            )
            continue

        with open(filename, "r") as f:
            content = f.read()
        
        status, formatted_content = __capitalize_first_character_of_sentence(content)

        if status == 1:
            # failed
            continue
        
        if not content == formatted_content:
            # Actual format happened
            count += 1
            # write data
            with open(filename, "w") as f:
                f.write(formatted_content)

            print(
                "{}{}FORMATTED: Sentences formatted for '{}'{}".format(
                    colors.BOLD, colors.OKGREEN, filename, colors.ENDC
                )
            )

    print(
        "{}{}TOTAL: {} files formatted.{}".format(
            colors.BOLD, colors.OKCYAN, count, colors.ENDC
        )
    )
