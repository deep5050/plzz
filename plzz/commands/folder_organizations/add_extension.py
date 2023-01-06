import os
import magic
from os import listdir
from os.path import isfile, join

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker



def __add_extension(filename):
    """
    Adds an extension to a file name if it is not present, depending on the file's type.

    Parameters:
    filename (str): The path to the file.

    Returns:
    str: The file name with the added extension.

    Raises:
    FileNotFoundError: If the file does not exist.
    ValueError: If the file type is not supported.
    """
    # Validate the file
    if not os.path.isfile(filename):
        print(
            "{}{}ERROR: file {} does not exist!{}".format(
                colors.BOLD, colors.FAIL, filename, colors.ENDC
            )
        )
        return
        # raise FileNotFoundError(f"The file {filename} does not exist.")

    # Get the file's extension
    _, file_ext = os.path.splitext(filename)

    # Check if the file has an extension
    if not file_ext:
        # Get the file's type
        file_type = magic.from_file(filename)

        # Determine the extension based on the file type
        if "ASCII text" in file_type:
            file_ext = ".txt"
        elif "Microsoft Word" in file_type:
            file_ext = ".doc"
        elif "PDF document" in file_type:
            file_ext = ".pdf"
        elif "PNG image" in file_type:
            file_ext = ".png"
        elif "JPEG image" in file_type:
            file_ext = ".jpg"
        else:
            print(
                "{}{}ERROR: File type {} not supported!{}".format(
                    colors.BOLD, colors.FAIL, file_type, colors.ENDC
                )
            )
            return
            # raise ValueError(f"The file type {file_type} is not supported.")

        # Add the extension to the file name
        filename += file_ext

    return filename


def __add_extensions_all_files(dirname):
    """
    Adds an extension to all file names under a directory if it is not present, depending on the file's type.

    Parameters:
    dirname (str): The path to the directory.


    Raises:
    FileNotFoundError: If the file does not exist.

    """

    # Validate the parameters
    if not os.path.isdir(dirname):
        print(
            "{}{}ERROR: directory {} does not exist!{}".format(
                colors.BOLD, colors.FAIL, dirname, colors.ENDC
            )
        )
        return
        # raise FileNotFoundError(f"The directory {dirname} does not exist.")
    count = 0
    onlyfiles = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    for _file in onlyfiles:
        file_path = os.path.abspath(os.path.join(os.path.curdir, dirname, _file))
        new_file_path = add_extension(file_path)

        if new_file_path == file_path:
            pass
        else:
            os.rename(file_path, new_file_path)
            count += 1

            print(
                "{}{}Renamed-> {} {}".format(
                    colors.BOLD, colors.OKCYAN, new_file_path, colors.ENDC
                )
            )

    print(
        "{}{}TOTAL: {} files renamed {}".format(
            colors.BOLD, colors.OKGREEN, count, colors.ENDC
        )
    )


def add_extensions_smartly(pathname):
    """Add missing extension to a file or all the files under a directory.

    Args:
        pathname (_type_): Path to a file or a directory.
    """
    count = 0
    files = []
    files = __pathname_checker(pathname)
    
    if len(files) == 0:
        return

    for file_path in files:
        new_file_path = __add_extension(file_path)
        if new_file_path == file_path:
            pass
        else:
            os.rename(file_path, new_file_path)
            count += 1

            print(
                "{}{}Renamed-> {} {}".format(
                    colors.BOLD, colors.OKCYAN, new_file_path, colors.ENDC
                )
            )

    print(
        "{}{}TOTAL: {} files renamed {}".format(
            colors.BOLD, colors.OKGREEN, count, colors.ENDC
        )
    )
