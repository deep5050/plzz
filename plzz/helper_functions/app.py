import requests
import json

from plzz.helper_functions.helper_functions import colors

# Update this during every release
VERSION = "0.2"

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
        "Run with {}`plzz --list`{} to see all the available commands. ".format(
            colors.OKCYAN, colors.ENDC
        )
    )

def __check_upstream_version():
    """
    check and notify if a latest version is available. if update available return True else False.
    """
    upstream_url = "https://pypi.org/pypi/plzz-cli/json"
    try:
        remote_data = requests.get(upstream_url)
        remote_data = remote_data.content.decode("utf8")
        remote_data = json.loads(remote_data)
        remote_version = remote_data["info"]["version"]

        # compare two version number
        tup_local = tuple(map(int, VERSION.split(".")))
        tup_remote = tuple(map(int, remote_version.split(".")))

        if tup_remote > tup_local:
            print("{}{}PLZZ: Update available ({}){}".format(
                colors.BOLD,
                colors.OKGREEN,
                remote_version,
                colors.ENDC 
            ))
            print("{}{}PLZZ: Run `pip3 install plzz-cli=={}`{}".format(
                colors.BOLD,
                colors.OKBLUE,
                remote_version,
                colors.ENDC
            ))
            

        else:
            print("{}{}PLZZ: No update available!{}".format(
                colors.BOLD,
                colors.OKGREEN,
                colors.ENDC 
            ))
    except:
        print("{}{}ERROR: Something went wrong during checking the update!{}".format(
            colors.BOLD,
            colors.FAIL,
            colors.ENDC
        ))