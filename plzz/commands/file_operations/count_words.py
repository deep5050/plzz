import string
import os

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __count_words(file_path: str, given_word: str) -> int:
    # Initialize the word count
    word_count = 0

    try:
        # Open the file
        with open(file_path, "r") as file:
            # Iterate over the lines in the file
            for line in file:
                # Split the line into words
                words = line.split()

                # Iterate over the words
                for word in words:
                    # Strip punctuation from the word
                    word = word.translate(str.maketrans("", "", string.punctuation))

                    # Increment the word count if the word is not empty
                    if word == given_word:
                        word_count += 1
    except:
        print("{}{}ERROR: Reading file '{}'! {}".format(
            colors.BOLD,
            colors.FAIL,
            file_path,
            colors.ENDC
        ))
    # Return the word count
    return word_count


def count_word_smartly(pathname: str, word: str):
    """Count number of words in a file or under all the files under a given directory.

    Args:
        pathname (str): Path to a file or a directory.
        word (str): Word to count.
    """
    files = __pathname_checker(pathname)
    count = 0

    for filepath in files:
        _ , file_ext = os.path.splitext(filepath)
        if not file_ext in ['.txt','.md','.log']:
            continue

        tmp_count = __count_words(filepath,word)
        if tmp_count > 0:
            print("{}{}FOUND: File '{}' has it {} time(s){}".format(
                colors.BOLD,
                colors.OKBLUE,
                filepath,
                tmp_count,
                colors.ENDC
            ))
            count += tmp_count
    print("{}{}TOTAL: Count for the word '{}' is {}{}".format(
        colors.BOLD,
        colors.OKGREEN,
        word,
        count,
        colors.ENDC
    ))


    
