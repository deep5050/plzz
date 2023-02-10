#!/usr/bin/env python

import sys
import os
import fire
import json

VERSION = "0.2"

# install module paths
sys.path.append("./plzz/helper_functions")
sys.path.append("./plzz/commands/file_operations")
sys.path.append("./plzz/commands/folder_organizations")



# import helper functions
from plzz.helper_functions.helper_functions import (
    colors,
    __list_all_commands,
    __search_command_by_keyword,
    __check_upstream_version,
     __populate_development_data,
)


# file operations
from plzz.commands.file_operations.create_random_text_files import create_random_text_files
from plzz.commands.file_operations.lorem_ipsum_file import create_lorem_ipsum_file
from plzz.commands.file_operations.generate_toc import generate_TOC_smartly
from plzz.commands.file_operations.count_words import count_word_smartly
from plzz.commands.file_operations.check_hash import check_hash_smartly
from plzz.commands.file_operations.offensive_words import detect_offensive_words_smartly, censor_offensive_words
from plzz.commands.file_operations.find_urls import find_urls_smartly
from plzz.commands.file_operations.format_sentences import format_sentences_smartly


# folder organizations
from plzz.commands.folder_organizations.add_extension import add_extensions_smartly
from plzz.commands.folder_organizations.delete_duplicates import delete_duplicate_files
from plzz.commands.folder_organizations.rename_files import rename_files_smartly
from plzz.commands.folder_organizations.delete_empty_files import delete_empty_text_files
from plzz.commands.folder_organizations.replace_word import replace_words_smartly
# from plzz.commands.folder_organizations.organize_audio_by_bits import move_audio_by_bitrate


# utilities
from plzz.commands.utilities.bing_wallpapers import  download_bing_wallpaper
from plzz.commands.utilities.generate_password import generate_password_smartly
from plzz.commands.utilities.qrcode import create_qr_code
from plzz.commands.utilities.extract_codeblocks_markdown import extract_code_blocks

# development
from plzz.commands.development_tasks.upload_to_gist import upload_to_gist_smartly
from plzz.commands.development_tasks.rename_functions import format_functions_smartly
from plzz.commands.development_tasks.licenses import add_license_smartly
from plzz.commands.development_tasks.minify_json import minify_json_files


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

def __print_about():
    """
    Print formatted about section of the app.
    """
    print(
        "{}{}PLZZ: A CLI to automate daily tasks.{}".format(
            colors.BOLD, colors.OKGREEN, colors.ENDC
        )
    )
    print("Version: {}".format(VERSION))
    print("Author: Dipankar Pal, Copyright MIT 2023")
    print("Github: https://github.com/deep5050/plzz")
    print(
        "Run with {}`plzz --list-commands`{} to see all the available commands. ".format(
            colors.OKCYAN, colors.ENDC
        )
    )

def __main__():
    fire.Fire(
        {
            "--about": __print_about,
            "--version": __print_version,
            "--update": __check_upstream_version,
            "--list": __list_all_commands,
            "--find": __search_command_by_keyword,
            # remove the below entry on deployment time 
            # "--develop": __populate_development_data,
            "create-random-text-files": create_random_text_files,
            "create-lorem-ipsum-file": create_lorem_ipsum_file,
            "generate-toc": generate_TOC_smartly,
            "add-missing-extensions": add_extensions_smartly,
            "delete-duplicates": delete_duplicate_files,
            "rename-files": rename_files_smartly,
            "format-sentences": format_sentences_smartly,
            "find-urls": find_urls_smartly,
            "count-offensive-words": detect_offensive_words_smartly,
            "censor-offensive-words": censor_offensive_words,
            "check-hash": check_hash_smartly,
            "delete-empty-files": delete_empty_text_files,
            "replace-words": replace_words_smartly,
            "count-word": count_word_smartly,
            "download-todays-wallpaper": download_bing_wallpaper,
            "upload-to-gist": upload_to_gist_smartly,
            # "format-function-names": format_functions_smartly,
            "generate-password": generate_password_smartly,
            # "check-password-strength": check_password_strength,
            "create-qr-code": create_qr_code,
            "add-license": add_license_smartly,
            "extract-code-blocks": extract_code_blocks,
            "minify-json": minify_json_files,
            # "organize-audio-by-bitrate": move_audio_by_bitrate
        }
    )

if __name__ == "__main__":
    __main__()
