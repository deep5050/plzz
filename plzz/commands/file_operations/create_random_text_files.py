import random
import string
import os


from plzz.helper_functions.helper_functions import colors



def create_random_text_files(num_files, directory):
    """
    Creates a specified number of random text files with random text under a given directory.

    Parameters:
    num_files (int): The number of files to create.
    directory (str): The path to the directory.

    Returns:
    None

    Raises:
    FileNotFoundError: If the directory does not exist.
    ValueError: If the number of files is not a positive integer.
    """

    # Validate the parameters
    if not os.path.isdir(directory):
        print(
            "{}{}ERROR: Directory '{}' does not exist!{}".format(
                colors.BOLD, colors.FAIL, directory, colors.ENDC
            )
        )
        return
        # raise FileNotFoundError(f"The directory {directory} does not exist.")
    if not isinstance(num_files, int) or num_files <= 0:
        print(
            "{}{}ERROR: Number of files should at least 1 !{}".format(
                colors.BOLD, colors.FAIL, colors.ENDC
            )
        )
        return
        # raise ValueError("The number of files must be a positive integer.")

    # Create the specified number of files
    for i in range(num_files):
        # Generate a random filename
        filename = "".join(random.choices(string.ascii_lowercase, k=10)) + ".txt"

        # Generate random content for the file
        content = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=1000)
        )
        print(
            "{}{}CREATED -> Random file '{}' created {}".format(
                colors.BOLD, colors.OKGREEN, filename, colors.ENDC
            )
        )

        # Write the content to the file
        with open(os.path.join(directory, filename), "w") as f:
            f.write(content)
