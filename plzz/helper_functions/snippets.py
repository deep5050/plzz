import ctypes
import os
from os import listdir
from os.path import isfile, isdir, join
from plzz.helper_functions.helper_functions import colors


def __pathname_checker(pathname: str) -> ctypes.Array:
    """check if the given path is a directory or a file name.

    Args:
        pathname (str): path to a file or a directory.

    Returns:
        ctypes.Array: list of file names.
    """
    files = []
    # check type file
    if isfile(pathname):
        files.append(pathname)
        return files
    elif isdir(pathname):
        files = [os.path.join(pathname, f) for f in listdir(pathname) if isfile(os.path.join(pathname, f))]
        return files
    else:
        print(
            "{}{}ERROR: path {} does not exist!{}".format(
                colors.BOLD, colors.FAIL, pathname, colors.ENDC
            )
        )
        return files
