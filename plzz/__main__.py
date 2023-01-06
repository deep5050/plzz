#!/usr/bin/env python

import sys
import os
import fire
import json

VERSION = "0.1"

# install module paths
sys.path.append("./plzz/helper_functions")
sys.path.append("./plzz/commands/file_operations")
sys.path.append("./plzz/commands/folder_organizations")



# import helper functions
from plzz.helper_functions.helper_functions import (
    colors,
    __list_all_commands,
    __group_available_commands,
    __search_command_by_keyword,
    __print_about,
    __check_upstream_version,
    # __make_function_database,
)


# file operations
from plzz.commands.file_operations.create_random_text_files import create_random_text_files
from plzz.commands.file_operations.lorem_ipsum_file import create_lorem_ipsum_file


# folder organizations
from plzz.commands.folder_organizations.add_extension import add_extensions_smartly
from plzz.commands.folder_organizations.delete_duplicates import delete_duplicate_files
from plzz.commands.folder_organizations.rename_files import rename_files_smartly
from plzz.commands.folder_organizations.delete_empty_files import delete_empty_text_files
from plzz.commands.folder_organizations.replace_word import replace_words_smartly



def __get_version():

    print("{}{} plzz (v{}) {}".format(
        colors.BOLD,
        colors.OKBLUE,
        VERSION,
        colors.ENDC
    ))
    return VERSION

def __print_version():

    print("{}{}plzz (v{}) {}".format(
        colors.BOLD,
        colors.OKBLUE,
        VERSION,
        colors.ENDC
    ))

def main():
    fire.Fire(
        {
            "--about": __print_about,
            "--version": __print_version,
            "--update": __check_upstream_version,
            "--list-commands": __group_available_commands,
            "--find-commands": __search_command_by_keyword,
            # "--update-commands-database": __make_function_database,
            "create-random-text-files": create_random_text_files,
            "create-lorem-ipsum-file": create_lorem_ipsum_file,
            "add-missing-extensions": add_extensions_smartly,
            "delete-duplicates": delete_duplicate_files,
            "rename-files": rename_files_smartly,
            "delete-empty-files": delete_empty_text_files,
            "replace-words": replace_words_smartly
        }
    )

if __name__ == "__main__":
    main()
