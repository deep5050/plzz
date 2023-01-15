
# TODO incomplete! 

import ast
import marshal
import os
import re


from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __rename_functions_javascript(filename: str,style: str, ) -> None:
    # Check if the file exists and is a JavaScript file
    # if not os.path.isfile(filename) or not filename.endswith(".js"):
    #     print("noooo")
    #     return

    # Read the JavaScript source code from the file
    with open(filename, "r") as f:
        source = f.read()

    # Parse the source code into an AST
    tree = ast.parse(source)

    # Iterate through the AST nodes
    for node in ast.walk(tree):
        # Check if the node is a function definition
        if isinstance(node, ast.FunctionDef):
            print(node.name)
            # Convert the function name to the specified style
            if style == "snakecase":
                node.name = re.sub(r"(?<!^)(?=[A-Z])", "_", node.name).lower()
            elif style == "kebabcase":
                node.name = re.sub(r"(?<!^)(?=[A-Z])", "-", node.name).lower()
            elif style == "camelcase":
                node.name = re.sub(r"_(\w)", lambda x: x.group(1).upper(), node.name)
            elif style == "pascalcase":
                node.name = re.sub(
                    r"_(\w)", lambda x: x.group(1).upper(), node.name
                ).capitalize()
            else:
                print("Error: Invalid style")
                return

    # Generate the modified source code from the AST
    modified_source = compile(tree, "<ast>", "exec")

    print(marshal.dumps(modified_source))
    # Write the modified source code to the file
    # with open(filename, "wb") as f:
    #     marshal.dump(modified_source,f)
    #     print("writing")

def __rename_functions_python(filename:str,style:str):
    pass



def format_functions_smartly(pathname: str, style: str):
    """Format all the function definitions with selected style (pascal/snakecase,kebabcase/camelcase).

    Args:
        pathname (str): Path to a file or directory.
        style (str): Preferred coding style.
    """
    if style.strip() not in ['kebacase','snakecase','camelcase','pascalcase']:
        print(
            "{}{}ERROR: Please choose your format style from (kebabcase,camelcase,pascalcase,snakecase){}!".format(
                colors.BOLD, colors.FAIL, colors.ENDC
            )
        )
        return

    total = 0

    files = __pathname_checker(pathname)

    for filename in files:
        if filename.endswith(".js"):
            # call javascript handler
            __rename_functions_javascript(filename,style)
            total += 1
            print("{}{}FORMATTED: File '{}'{}".format(
                colors.BOLD,
                colors.OKGREEN,
                filename,
                colors.ENDC
            ))

        elif filename.endswith(".py"):
            # call python handler
            __rename_functions_javascript(filename,style)
            total += 1
            print("{}{}FORMATTED: File '{}'{}".format(
                colors.BOLD,
                colors.OKGREEN,
                filename,
                colors.ENDC
            ))
            print("python")
            
        elif filename.endswith(".c") or filename.endswith(".cpp"):
            # call cpp handler
            print("cpp")
