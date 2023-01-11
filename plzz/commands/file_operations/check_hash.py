import hashlib

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __check_hash_md5(filepath: str) -> str:
    """Encrypt a given file with the MD5 hash function and return the key.

    This function reads the specified file, calculates the MD5 hash of its contents, and returns the hexadecimal representation of the hash as a string.

    Args:
        filepath: The path to the file to be encrypted.

    Returns:
        The hexadecimal representation of the MD5 hash of the file contents.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        OSError: If there is an error reading the file.
    """
    # Initialize the MD5 hash function
    m = hashlib.md5()

    try:
        # Read the file and update the hash with its contents
        with open(filepath, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                m.update(data)

        # Return the hexadecimal representation of the hash
        return m.hexdigest()
    except:
        print(
            "{}{}ERROR: Encrypting file '{}'!{}".format(
                colors.BOLD, colors.FAIL, filepath, colors.ENDC
            )
        )
        return False


def check_hash_smartly(pathname: str):
    """Encrypt a file (MD5) or all the files under a directory and print the key(s).

    Args:
        pathname (str): Path to a file or directory.
    """

    files = __pathname_checker(pathname)

    count = 0
    for filepath in files:
        tmp_key = __check_hash_md5(filepath)
        if tmp_key == False:
            pass
        else:
            print(
                "{}{}HASH: MD5 for file '{}' is '{}'{}".format(
                    colors.BOLD, colors.OKBLUE, filepath, tmp_key, colors.ENDC
                )
            )
            count += 1

    print(
        "{}{}TOTAL: {} Hashes generated".format(
            colors.BOLD, colors.OKGREEN, count, colors.ENDC
        )
    )
