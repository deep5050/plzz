import os
import re

from plzz.helper_functions.helper_functions import colors

def extract_code_blocks(markdown_file):
    """Extract code blocks from a markdown file and create separate files for each code block.

    Args:
        markdown_file (str): The path to the markdown file.

    Returns:
        None
    """
    if not os.path.isfile(markdown_file):
        print("{}{}ERROR: '{}' No such file exists!{}".format(
            colors.BOLD,
            colors.FAIL,
            markdown_file,
            colors.ENDC
        ))
        return

    _, file_extension = os.path.splitext(markdown_file)
    
    if not file_extension == ".md":
        print("{}{}ERROR: '{}' is not a markdown file {}!".format(
            colors.BOLD,
            colors.FAIL,
            markdown_file,
            colors.ENDC
        ))
        return

    try:
        # Open the markdown file
        with open(markdown_file, 'r') as f:
            # Read the contents of the file
            contents = f.read()

        # Use a regular expression to extract the code blocks from the file
        code_blocks = re.findall(r'```(.*?)```', contents, re.DOTALL)
        for i, code_block in enumerate(code_blocks):
            # Extract the language of the code block
            language = re.search(r'^([^\n]+)\n', code_block).group(1)

            # Generate a filename based on the language and the index of the code block
            filename = f'code_{language}_{i}.{language.lower()}'

            # Write the code block to the file
            with open(filename, 'w') as f:
                f.write(code_block)

    except Exception as e:
        # Print an error message if an exception occurs
        print("{}{}ERROR: Something went wrong!{}".format(
            colors.BOLD,
            colors.FAIL,
            colors.ENDC
        ))