import os

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __rename_file(filename, old_char, new_char):
    """
    Renames a given file by replacing a specific character with a new one.

    Parameters:
    filename (str): The path to the file to rename.
    old_char (str): The character to replace.
    new_char (str): The character to replace with.

    Returns:
    None

    Raises:
    FileNotFoundError: If the file does not exist.
    ValueError: If the old character is not a single character or the new character is not a single character.
    """
    # Validate the file
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    # Validate the old character
    if len(old_char) != 1:
        raise ValueError(f"The old character {old_char} is not a single character.")

    # Get the file's directory and base name
    directory, basename = os.path.split(filename)

    filename, ext = os.path.splitext(basename)

    # Replace the old character with the new character in the base name
    new_basename = filename.replace(old_char, new_char) + ext

    # Construct the new file path
    new_filename = os.path.join(directory, new_basename)

    # return new file name
    return new_filename


def rename_files_smartly(pathname: str, old_char: str, new_char="") -> None:
    """Rename a file/all files under directory by replacing specified character with new one.

    Args:
        pathname (str): Path to a file or a directory.
        old_char (str): Character to be replaced.
        new_char (str): Character to be replaced with.
    """

    if old_char == "space":
        old_char = " "
    elif old_char == "dash":
        old_char = "-"
    elif old_char == "underscore":
        old_char = "_"
    elif old_char == "dot":
        old_char = "."
    else:
        pass

    if not new_char:
        new_char = ""
    elif new_char == "space":
        new_char = " "
    elif new_char == "dash":
        new_char = "-"
    elif new_char == "underscore":
        new_char = "_"
    elif new_char == "dot":
        new_char = "."
    elif new_char == "nothing":
        new_char = ""
    else:
        pass

    files = __pathname_checker(pathname)

    count = 0
    for file_path in files:
        new_filepath = __rename_file(file_path, old_char, new_char)
        print(new_filepath)
        os.rename(file_path, new_filepath)
        count += 1

        print(
            "{}{}Renamed-> {} {}".format(
                colors.BOLD, colors.OKCYAN, new_filepath, colors.ENDC
            )
        )

    print(
        "{}{}TOTAL: {} files renamed {}".format(
            colors.BOLD, colors.OKGREEN, count, colors.ENDC
        )
    )
