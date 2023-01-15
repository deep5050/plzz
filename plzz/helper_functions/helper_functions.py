import json
import os
import ast
from pathlib import Path

from plzz.helper_functions.commands_database import functions, commands, commands_map

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

function_database = "data/functions.json"
command_mapping = "data/commands_mapping.json"

# run the function to generate commands_map.database
def __make_commands_mapping():
    
    # get keys from commands.databse, get the the data against the key (function name)
    # feed the function name into function.database
    # group the result based on their doc strings
    commands_types = []
    commands_map = []

    for _command in commands.database:
        if _command.startswith("--"):
            # Commands for plzz itself
            continue

        tmp = {}
        command_name = _command
        function_name = commands.database[_command]
        function_group = functions.database[function_name].split(":")[0]
        function_doc = functions.database[function_name].split(":")[1]

        tmp['command'] = command_name
        tmp["function"] = function_name
        tmp["doc"] = function_doc
        tmp['category'] = function_group
        
        if function_group not in commands_types:
            commands_types.append(function_group)
        
        commands_map.append(tmp)

    with open(command_mapping,"w") as f:
        json.dump(commands_map,f)

    return commands_map


def __group_available_commands():
    """Group available commands by their type/dirname and return a dict.
    """
    command_types = []
    
    # get unique commands types
    for command in commands_map.database:
        if command['category'] not in command_types:
            command_types.append(command['category'])
        
    for command_type in command_types:
        print("\n{}{}{}{}".format(
            colors.BOLD,
            colors.OKBLUE,
            command_type.replace("_", " ").upper(),
            colors.ENDC
        ))

        for command_object in commands_map.database:
            if command_object["category"] == command_type:
                print("{}{}{}{} : {}".format(
                    colors.BOLD,
                    colors.OKGREEN,
                    command_object['command'],
                    colors.ENDC,
                    command_object['doc']
                ))
 

def __list_all_commands():
    """
    List all the available commands for the app.
    """
    __group_available_commands()



# search commands
def __search_commands(keyword:str):
    pass


# helper function to find commands from a given keyword
# here we need a complete list of available function names
def __search_command_by_keyword(keyword):
    """
    Searches a command by given keyword.

    Parameters:
    keyword (str): The keyword to search for.

    Raises:
    FileNotFoundError: If the JSON file does not exist.
    """
    
    data = commands_map.database
    # Iterate over the keys in the data
    for command in data:
        # Split the key into parts
        command_str_arr = command['command'].split("-")

        # Check if any of the parts match the keyword
        if any(part == keyword for part in command_str_arr):
            # exclude type of functions from the docstring (split with :)
            print(
                "{}{}{}{} : {}".format(
                    colors.BOLD,
                    colors.OKBLUE,
                    command['command'],
                    colors.ENDC,
                    command['doc'],
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
                    # print(name)
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

    with open(function_database,'w') as f:
        json.dump(function_dict,f)


def __populate_development_data():
    __make_function_database("plzz")
    print("1. update 'snippets/function.database' with the content in 'data/functions.json' now !")
    print("2. update 'snippets/commands.database' with the content in '__main__.py' now !")
    __make_commands_mapping()
    print("3. update 'snippets/commands_map.database' with the content in 'data/commands_mapping.json' now !")
    
