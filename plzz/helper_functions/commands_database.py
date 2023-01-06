import json
import os


class Commands(object):
    def __init__(self) -> None:
        self.database = {
            "create_random_text_files": "file_operations:Creates a specified number of random text files with random text under a given directory.",
            "create_lorem_ipsum_file": "file_operations:Creates a Lorem Ipsum file with a specified number of lines.",
            "add_extensions_smartly": "folder_organizations:Add missing extension to a file or all the files under a directory.",
            "delete_duplicate_files": "folder_organizations:Generates the MD5 hash of all the files in a given directory and deletes one of the files if two hashes match.",
            "delete_empty_text_files": "folder_organizations:Delete all empty text files from src_dir.",
            "rename_files_smartly": "folder_organizations:Rename a file/all files under directory by replacing specified character with new one.",
            "replace_words_smartly": "folder_organizations:Replace all the words in a given file or all the files under a directory with a new word.",
        }


commands = Commands()
