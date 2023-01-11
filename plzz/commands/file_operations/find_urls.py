import os
import re
import glob


from plzz.helper_functions.snippets import __pathname_checker
from plzz.helper_functions.helper_functions import colors


def __all_links_in_directory(file_path: str, output_file_path: str) -> None:
    # Compile the regular expression pattern for matching URLs
    pattern = re.compile(
        r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
    )
    count = 0
    # Create the output file
    # with open(output_file_path, "a") as output_file:
    data = ""
    with open(file_path, "r") as file:
        # Read the file content
        content = file.read()

        # Find all the URLs in the content
        links = pattern.findall(content)

        # Iterate over the links

        for link in links:
            # Write the link to the output file
            data += "{}\n".format(link[0] + "://" + link[1] + link[2])
            count += 1
    return count, data


def find_urls_smartly(pathname: str, outfile: str):
    """Find all the links from a text file or all the text files under a directory.

    Args:
        pathname (str): Path to a file or a directory.
        outfile (str): Output filename with all the URLs in it.
    """
    files = __pathname_checker(pathname)
    total = 0
    data = ""
    for filename in files:
        count = 0
        count, tmp_data = __all_links_in_directory(filename, outfile)

        if not count == 0:
            print(
                "{}{}FOUND: '{}' URLs in file '{}' {}".format(
                    colors.BOLD, colors.OKGREEN, count, os.path.basename(filename), colors.ENDC
                )
            )
            data = "{}\n# {}\n{}".format(data, filename, tmp_data)

        total += count

    print(
        "{}{}TOTAL: {} URLS found".format(
            colors.BOLD, colors.OKGREEN, total, colors.ENDC
        )
    )
    with open(outfile, "w") as f:
        f.write(data)
