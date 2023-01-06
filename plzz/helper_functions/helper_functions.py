import json
import os
import ast
from pathlib import Path

from plzz.helper_functions.commands_database import commands
# ANSI colors
class Colors(object):
    def __init__(self) -> None:
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

colors = Colors()


home = str(Path.home())



functions_database = os.path.join(home,"functions.json")


# group commands from functions.json file
def __group_available_commands():
    """
    Group available commands by their type/dirname and return a dict.
    """
    commands_types = []

    data = ""
    # with open(functions_database, "r") as f:
    data = commands.database
    for key in data:
        # get the command type
        command_type = data[key].split(":")[0].strip()

        # list unique types of commands
        if not command_type in commands_types:
            commands_types.append(command_type)

    # group commands
    for types in commands_types:
        command_type_str = str(types).replace("_", " ").upper()
        print(
            "{}{}{}:{}".format(
                colors.BOLD, colors.OKGREEN, command_type_str, colors.ENDC
            )
        )
        for command in data:
            if types in data[command]:
                print(
                    "{}{}{} : {}".format(
                        colors.OKBLUE, command.replace("_","-"), colors.ENDC, data[command].split(":")[1]
                    )
                )



def __list_all_commands():
    """
    List all the available commands for the app.
    """
    __group_available_commands()


# helper function to find commands from a given keyword
# here we need a complete list of available function names
def __search_command_by_keyword(keyword):
    """
    Searches a JSON file for keys that contain a given keyword (where the keys are underscore-separated strings).

    Parameters:
    keyword (str): The keyword to search for.

    Raises:
    FileNotFoundError: If the JSON file does not exist.
    """

    # Validate the parameters
    # if not os.path.isfile(functions_database):
    #     raise FileNotFoundError(
    #         f"The function database: {functions_database} does not exist."
    #     )

    # # Open the JSON file
    # with open(functions_database, "r") as f:
    #     # Load the file contents
    #     data = json.load(f)
    # commands.update()
    data = commands.database
    # Iterate over the keys in the data
    for key in data:
        # Split the key into parts
        parts = key.split("_")

        # Check if any of the parts match the keyword
        if any(part == keyword for part in parts):
            # exclude type of commands from the docstring (split with :)
            print(
                "{}{}{}{} : {}".format(
                    colors.BOLD,
                    colors.OKBLUE,
                    key,
                    colors.ENDC,
                    data[key].split(":")[1],
                )
            )


def __print_about():
    """
    Print formatted about section of the app.
    """
    print(
        "{}{}PLZZ: A CLI to automate daily tasks.{}".format(
            colors.BOLD, colors.OKGREEN, colors.ENDC
        )
    )
    print("Version: {}".format("0.1"))
    print("Author: Dipankar Pal, Copyright MIT 2023")
    print("Github: https://github.com/deep5050/plzz")
    print(
        "Run with {}`plzz list_commands`{} to see all the available commands. ".format(
            colors.OKCYAN, colors.ENDC
        )
    )


def __check_upstream_version():
    """
    check and notify if a latest version is available.
    """
    pass


def __find_python_files(directory):
    """
    Finds all the python files under a given directory.
    
    Parameters:
    directory (str): The path to the directory.
    
    Returns:
    list: A list of the python files.
    
    Raises:
    FileNotFoundError: If the directory does not exist.
    """
    # Validate the parameter
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Initialize the list of python files
    python_files = []
    
    # Iterate over the files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a python file
            if file.endswith(".py"):
                # Add the file to the list
                python_files.append(os.path.join(root, file))
    
    return python_files

## to be used in development mode
def __extract_function_info(python_filename):
    """
    Extracts the function names and descriptions (if any) from the docstrings in a given python file, and writes them to a JSON file.
    
    Parameters:
    python_filename (str): The name of the python file.
    
    Returns:
    function_info (dict): The name and description of the functions as a dict
    
    Raises:
    FileNotFoundError: If the python file does not exist.
    """


    # Initialize the function info
    function_info = {}

    # exclude functions keyword
    exclude_keyword = '__'

    # Parse the python file
    with open(python_filename, "r") as f:
        tree = ast.parse(f.read())
    

    command_type = os.path.dirname(python_filename) 
    command_type = os.path.basename(command_type)

    # Iterate over the functions in the tree
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Extract the function name and docstring
            name = node.name
            
            # excluding functions from entering database
            if not exclude_keyword in name:
                # print(name)
                try:
                    docstring = ast.get_docstring(node)
                    
                    # Add the function info (first line only) to the dictionary
                    function_info[name] = "{}:{}.".format(command_type,docstring.split(".")[0].strip())
                except:
                    function_info[name] = "{}:{}".format(command_type,'N/A')
    
    return function_info


## to be used in development mode
def __make_function_database(dirname):
    """ Extract all the function names from all the python files from a given directory

    """

    python_files = __find_python_files(dirname)
    
    function_dict = {}

    for file_name in python_files:
        new_function_dict = __extract_function_info(file_name)
        # merge two dicts
        function_dict = {**function_dict, **new_function_dict}
        # function_dict = function_dict | new_function_dict

    with open(functions_database,'w') as f:
        json.dump(function_dict,f)
    commands.update()