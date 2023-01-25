# update this class by calling `--develop`
class Functions(object):
    def __init__(self) -> None:
        self.database = {
    "add_license_smartly": "development_tasks:Create a license file of desired type.",
    "format_functions_smartly": "development_tasks:Format all the function definitions with selected style (pascal/snakecase,kebabcase/camelcase).",
    "upload_to_gist_smartly": "development_tasks:Upload a file or all files under a directory to Github Gist.",
    "check_hash_smartly": "file_operations:Encrypt a file (MD5) or all the files under a directory and print the key(s).",
    "count_word_smartly": "file_operations:Count number of words in a file or under all the files under a given directory.",
    "create_random_text_files": "file_operations:Creates a specified number of random text files with random text under a given directory.",
    "find_urls_smartly": "file_operations:Find all the links from a text file or all the text files under a directory.",
    "format_sentences_smartly": "file_operations:Format each sentences correctly in a english text a file or all files under a directory.",
    "generate_TOC_smartly": "file_operations:Generate Table of contents from a given markdown file or all the markdown files under a directory.",
    "create_lorem_ipsum_file": "file_operations:Creates a Lorem Ipsum file with a specified number of lines.",
    "detect_offensive_words_smartly": "file_operations:Count offensive words from a file or a directory.",
    "censor_offensive_words": "file_operations:Censor offensive words from a file or all files under a directory.",
    "add_extensions_smartly": "folder_organizations:Add missing extension to a file or all the files under a directory.",
    "delete_duplicate_files": "folder_organizations:Generates the MD5 hash of all the files in a given directory and deletes one of the files if two hashes match.",
    "delete_empty_text_files": "folder_organizations:Delete all empty text files from src_dir.",
    "rename_files_smartly": "folder_organizations:Rename a file/all files under directory by replacing specified character with new one.",
    "replace_words_smartly": "folder_organizations:Replace all the words in a given file or all the files under a directory with a new word.",
    "download_bing_wallpaper": "utilities:Download today's wallpaper from bing, and save them.",
    "generate_password_smartly": "utilities:Generate a password of a given strength (low,medium,strong) or any specific length.",
    "create_qr_code": "utilities:Create qr code and save it as a image."
}


# update this class manually from __main__
class Commands(object):
    def __init__(self) -> None:
        # mapping between commands and actual function to be called
        self.database = {
            "--about": "__print_about",
            "--version": "__print_version",
            "--update": "__check_upstream_version",
            "--list-commands": "__list_all_commands",
            "--find-commands": "__search_command_by_keyword",
            # remove the below entry on deployment time
            "--develop": "__populate_development_data",
            "create-random-text-files": "create_random_text_files",
            "create-lorem-ipsum-file": "create_lorem_ipsum_file",
            "generate-toc": "generate_TOC_smartly",
            "add-missing-extensions": "add_extensions_smartly",
            "delete-duplicates": "delete_duplicate_files",
            "rename-files": "rename_files_smartly",
            "format-sentences": "format_sentences_smartly",
            "find-urls": "find_urls_smartly",
            "count-offensive-words": "detect_offensive_words_smartly",
            "censor-offensive-words": "censor_offensive_words",
            "check-hash": "check_hash_smartly",
            "delete-empty-files": "delete_empty_text_files",
            "replace-words": "replace_words_smartly",
            "count-word": "count_word_smartly",
            "download-todays-wallpaper": "download_bing_wallpaper",
            "upload-to-gist": "upload_to_gist_smartly",
            "generate-password": "generate_password_smartly",
            "create-qr-code": "create_qr_code",
            "add-license": "add_license_smartly"
        }


# update this class by calling `--develop`
class Commands_map(object):
    def __init__(self) -> None:
        self.database = [
    {
        "command": "create-random-text-files",
        "function": "create_random_text_files",
        "doc": "Creates a specified number of random text files with random text under a given directory.",
        "category": "file_operations"
    },
    {
        "command": "create-lorem-ipsum-file",
        "function": "create_lorem_ipsum_file",
        "doc": "Creates a Lorem Ipsum file with a specified number of lines.",
        "category": "file_operations"
    },
    {
        "command": "generate-toc",
        "function": "generate_TOC_smartly",
        "doc": "Generate Table of contents from a given markdown file or all the markdown files under a directory.",
        "category": "file_operations"
    },
    {
        "command": "add-missing-extensions",
        "function": "add_extensions_smartly",
        "doc": "Add missing extension to a file or all the files under a directory.",
        "category": "folder_organizations"
    },
    {
        "command": "delete-duplicates",
        "function": "delete_duplicate_files",
        "doc": "Generates the MD5 hash of all the files in a given directory and deletes one of the files if two hashes match.",
        "category": "folder_organizations"
    },
    {
        "command": "rename-files",
        "function": "rename_files_smartly",
        "doc": "Rename a file/all files under directory by replacing specified character with new one.",
        "category": "folder_organizations"
    },
    {
        "command": "format-sentences",
        "function": "format_sentences_smartly",
        "doc": "Format each sentences correctly in a english text a file or all files under a directory.",
        "category": "file_operations"
    },
    {
        "command": "find-urls",
        "function": "find_urls_smartly",
        "doc": "Find all the links from a text file or all the text files under a directory.",
        "category": "file_operations"
    },
    {
        "command": "count-offensive-words",
        "function": "detect_offensive_words_smartly",
        "doc": "Count offensive words from a file or a directory.",
        "category": "file_operations"
    },
    {
        "command": "censor-offensive-words",
        "function": "censor_offensive_words",
        "doc": "Censor offensive words from a file or all files under a directory.",
        "category": "file_operations"
    },
    {
        "command": "check-hash",
        "function": "check_hash_smartly",
        "doc": "Encrypt a file (MD5) or all the files under a directory and print the key(s).",
        "category": "file_operations"
    },
    {
        "command": "delete-empty-files",
        "function": "delete_empty_text_files",
        "doc": "Delete all empty text files from src_dir.",
        "category": "folder_organizations"
    },
    {
        "command": "replace-words",
        "function": "replace_words_smartly",
        "doc": "Replace all the words in a given file or all the files under a directory with a new word.",
        "category": "folder_organizations"
    },
    {
        "command": "count-word",
        "function": "count_word_smartly",
        "doc": "Count number of words in a file or under all the files under a given directory.",
        "category": "file_operations"
    },
    {
        "command": "download-todays-wallpaper",
        "function": "download_bing_wallpaper",
        "doc": "Download today's wallpaper from bing, and save them.",
        "category": "utilities"
    },
    {
        "command": "upload-to-gist",
        "function": "upload_to_gist_smartly",
        "doc": "Upload a file or all files under a directory to Github Gist.",
        "category": "development_tasks"
    },
    {
        "command": "generate-password",
        "function": "generate_password_smartly",
        "doc": "Generate a password of a given strength (low,medium,strong) or any specific length.",
        "category": "utilities"
    },
    {
        "command": "create-qr-code",
        "function": "create_qr_code",
        "doc": "Create qr code and save it as a image.",
        "category": "utilities"
    },
    {
        "command": "add-license",
        "function": "add_license_smartly",
        "doc": "Create a license file of desired type.",
        "category": "development_tasks"
    }
]

functions = Functions()
commands = Commands()
commands_map = Commands_map()
