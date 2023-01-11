import re
import os

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __generate_toc(markdown_file):
    """Generate a table of contents for a markdown file and append it to the beginning of the same file.

    Args:
        markdown_file (str): The path to the markdown file.

    Returns:
        None
    """
    if not os.path.isfile(markdown_file):
        print(
            "{}{}ERROR: File '{}' does not exist!{}".format(
                colors.BOLD, colors.FAIL, markdown_file, colors.ENDC
            )
        )
        return False



    try:
        # Open the markdown file
        with open(markdown_file, "r") as f:
            # Read the contents of the file
            contents = f.read()

        # Use a regular expression to extract the headings from the file
        headings = re.findall(r"^(#+)(.*?)$", contents, re.MULTILINE)

        # Generate the TOC
        toc = "\n"
        for level, heading in headings:
            # Create a link to the heading
            link = (
                "- ["
                + heading.strip()
                + "](#"
                + heading.strip().lower().replace(" ", "-")
                + ")"
            )
            toc += "  " * (len(level) - 1) + link + "\n"

        # Insert the TOC at the beginning of the file
        contents = toc + "\n" + contents

        # Write the modified contents back to the file
        with open(markdown_file, "w") as f:
            f.write(contents)
        return True
    except Exception as e:
        print(
            "{}{}ERROR: Something went wrong while reading '{}'!{}".format(
                colors.BOLD, colors.FAIL, markdown_file, colors.ENDC
            )
        )
        return False


def generate_TOC_smartly(pathname: str):
    """Generate Table of contents from a given markdown file or all the markdown files under a directory.

    Args:
        pathname (str): Path to a file or a directory.
    """
    files = __pathname_checker(pathname)
    count = 0
    for filepath in files:
        _ , file_ext = os.path.splitext(filepath)
    
        if not "md" in file_ext:
            if len(files) == 1:
                # only a single file provided and that's not a markdown
                # notify user
                
                print("{}{}ERROR: File '{}' is not a markdown one with '.md' extension! {}".
                format(
                    colors.BOLD,
                    colors.FAIL,
                    filepath,
                    colors.ENDC
                ))
            
            continue
    
        flag = __generate_toc(filepath)
        if flag == True:
            print(
                "{}{}GENERATED: TOC added for the file '{}' {}".format(
                    colors.BOLD, colors.OKGREEN, filepath, colors.ENDC
                )
            )

            count += 1
    print(
        "{}{}TOTAL: {} files modified.{}".format(
            colors.BOLD, colors.OKBLUE, count, colors.ENDC
        )
    )
