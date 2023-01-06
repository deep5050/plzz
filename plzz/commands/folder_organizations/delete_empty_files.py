import os

from plzz.helper_functions.helper_functions import colors


def delete_empty_text_files(dirname):
    """Delete all empty text files from src_dir.

    Args:
    - dirname (str): the directory to search for empty text files

    Returns:
    - None
    """
    if not os.path.isdir(dirname):
        print(
            "{}{}ERROR: Directory {} does not exist!{}".format(
                colors.BOLD, colors.FAIL, dirname, colors.ENDC
            )
        )

        return

    count = 0

    # Iterate through all files in the source directory
    for filename in os.listdir(dirname):
        # Check if the file is a text file
        if filename.endswith(
            (
                ".txt",
                ".py",
                ".c",
                ".cpp",
                ".java",
                ".html",
                ".css",
                ".js",
                ".cs",
                ".h",
                ".sh",
                ".bat",
                ".log",
            )
        ):
            src_path = os.path.join(dirname, filename)

            # Check if the file is empty
            try:
                with open(src_path, "r") as f:
                    contents = f.read()
                    if not contents:
                        # The file is empty, so delete it
                        os.remove(src_path)
                        count += 1
                        print(
                            "{}{}REMOVING -> '{}'{}".format(
                                colors.BOLD, colors.OKGREEN, src_path, colors.ENDC
                            )
                        )

            except Exception as e:
                # If there is an error reading the file, it is likely corrupt
                print(
                    "{}{}ERROR: Reading '{}' !{}".format(
                        colors.BOLD, colors.FAIL, src_path, colors.ENDC
                    )
                )
    print(
        "{}{}TOTAL: {} files removed {}".format(
            colors.BOLD, colors.OKGREEN, count, colors.ENDC
        )
    )
