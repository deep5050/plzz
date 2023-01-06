import os

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __replace_word(file_name, old_word, new_word):
    """
    Replaces a specified word in all the files in a directory with a new word.

    Parameters:
    - dirname (str): The path of the directory.
    - old_word (str): The word to be replaced.
    - new_word (str): The replacement word.

    Returns:
    None
    """
    if not os.path.isfile(file_name):
        print(
            "{}{}ERROR: '{}' does not exist!{}".format(
                colors.BOLD, colors.FAIL, file_name, colors.ENDC
            )
        )
        return

    try:
        # Open the file
        with open(file_name, "r") as f:
            contents = f.read()
            # Replace the word in the file
            tmp_contents = contents
            contents = contents.replace(old_word, new_word)
            if tmp_contents == contents:
                return False
    
        # Write the modified contents back to the file
        with open(file_name, "w") as f:
            f.write(contents)
    except OSError as e:
            print(
            "{}{}ERROR: '{}' could not be modified!{}".format(
                colors.BOLD, colors.FAIL, file_name, colors.ENDC
            )
        )


def replace_words_smartly(pathname:str,old_word:str,new_word:str):
    """ Replace all the words in a given file or all the files under a directory with a new word.

    Args:
        pathname (str): Path to a file or a directory.
        old_word (str): Word to replaced.
        new_word (str): Word to be replaced with.
    """
    files = __pathname_checker(pathname)
    for file_name in files:
        flag = __replace_word(file_name,old_word,new_word)
        if flag == False:
            pass
        else:
            print(
            "{}{}MODIFIED -> '{}'{}".format(
                colors.BOLD, colors.OKGREEN, file_name, colors.ENDC
            )
        )

    
    
        
