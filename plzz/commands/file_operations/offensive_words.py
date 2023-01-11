import os

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker

# WARNING !!!

# Please be aware that using this words is considered as hate speech and it can be taken as offensive. 
# These words are used to insult and demean people based on their race, ethnicity, sexual orientation, 
# gender identity, and other characteristics. 
# It's important to be aware of the potential harm that these words can cause, 
# and use them only in appropriate and necessary contexts, if at all.

# It's also worth noting that this list is not exhaustive, 
# and offensive language can take many forms. Different cultures, communities, 
# and individuals have different norms and standards when it comes to 
# what is considered offensive or insensitive, 
# so it's important to keep that in mind when trying to identify and filter out offensive words.


offensive_words = [
    "nigger",
    "fag",
    "faggot",
    "cunt",
    "nigga",
    "dick",
    "pussy",
    "slut",
    "whore",
    "chink",
    "kike",
    "dyke",
    "bitch",
    "retard",
    "tranny",
    "cocksucker",
    "niggers",
    "fags",
    "faggots",
    "cunts",
    "niggas",
    "dicks",
    "pussies",
    "sluts",
    "whores",
    "chinks",
    "kikes",
    "dykes",
    "bitches",
    "retards",
    "trannies",
    "cocksuckers",
]


def __censor_word(word):
    if len(word) < 3:
        return word
    else:
        return word[0] + "*" * (len(word) - 2) + word[-1]


def __defect_offensive_words(filename: str):
    """Find offensive words from a file.

    Args:
        filename (str): Path to a file.
    """

    count = 0
    try:
        with open(filename, "r") as f:
            contents = f.read()
            # Iterate over the lines in the file
            for i, line in enumerate(contents.split("\n")):
                for word in offensive_words:
                    if word in line.lower():
                        count += line.count(word)
            return count
    except:
        print(
            "{}{}ERROR: Reading file '{}'!".format(
                colors.BOLD, colors.FAIL, filename, colors.ENDC
            )
        )
        return 0


def detect_offensive_words_smartly(pathname: str):
    """Count offensive words from a file or a directory.

    Args:
        pathname (str): Path to a file or a directory.
    """
    print(
        "{}{}WARNING: This may not detect some words!".format(
            colors.WARNING, colors.BOLD, colors.ENDC
        )
    )

    files = __pathname_checker(pathname)
    total = 0
    for filepath in files:
        count = 0
        count = __defect_offensive_words(filepath)
        if not count == 0:
            print(
                "{}{}FOUND: {} offensive words in '{}' {}".format(
                    colors.BOLD, colors.OKGREEN, count, filepath, colors.ENDC
                )
            )
        total += count

    print(
        "{}{}TOTAL: {} offensive words found{}".format(
            colors.BOLD, colors.OKBLUE, total, colors.ENDC
        )
    )


def __encode_offensive_words(filename: str):
    """Encode offensive words in a file. example "fuck" -> "f**k".

    Args:
        filename (str): Path to a file.
    """
    count = 0
    new_data = ""

    try:
        with open(filename, "r") as f:
            contents = f.read()
            # Iterate over the lines in the file
            for i, line in enumerate(contents.split("\n")):
                tmp_line = line
                for word in offensive_words:
                    if word in line.lower():
                        # replace the word
                        tmp_line = tmp_line.replace(word, __censor_word(word))

                        # TODO remove
                        # print(__censor_word(word))
                        count += line.count(word)

                new_data += tmp_line + "\n"

        with open(filename, "w") as f:
            f.write(new_data)

        return count

    except:
        print(
            "{}{}ERROR: Reading file '{}'!".format(
                colors.BOLD, colors.FAIL, filename, colors.ENDC
            )
        )
        return 0


def censor_offensive_words(pathname: str):
    """Censor offensive words from a file or all files under a directory. Example: "f**k".

    Args:
        pathname (str): Path to a file or a directory.
    """

    files = __pathname_checker(pathname)
    total = 0

    for filepath in files:
        count = 0
        count = __encode_offensive_words(filepath)
        if not count == 0:
            print(
                "{}{}CENSORED: {} offensive words in file '{}' {}".format(
                    colors.BOLD, colors.OKGREEN, count, filepath, colors.ENDC
                )
            )
        total += count

    print(
        "{}{}TOTAL: {} offensive words censored{}".format(
            colors.BOLD, colors.OKBLUE, total, colors.ENDC
        )
    )
