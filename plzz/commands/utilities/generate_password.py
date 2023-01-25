import random
import string
import re


from plzz.helper_functions.helper_functions import colors


# import pwgen

def __version2(length=12, num=1, symbols=True, capitalize=True):
    return pwgen.pwgen(length=length, count=num, symbols=symbols, capitalize=capitalize)

# length = int(input("Enter the desired length of the password: "))
# password = suggest_password(length)
# print("Suggested password:", password)

def __has_english_characters(string):
    english_characters = re.compile(r'[a-zA-Z]')
    return bool(english_characters.search(string))

def __generate_password(length):
    return "".join(
        random.choice(string.ascii_letters + string.digits + string.punctuation)
        for i in range(length)
    )


def generate_password_smartly(strength: str):
    """Generate a password of a given strength (low,medium,strong) or any specific length.

    Args:
        strength (str): Strength of a password (low/medium/strong) ar any given length like (4/9/16).
    """
    strength = str(strength)

    if not strength:
        print(
            "{}{}ERROR: Please specify the strength (low/medium/string) ar any given length like 4.{}".format(
                colors.BOLD, colors.FAIL, colors.ENDC
            )
        )
        return
    length = 0
    if str(strength).lower() == "strong":
        length = 12
    elif str(strength).lower() == "medium":
        length = 8
    elif str(strength).lower() == "low":
        length = 4
    # any other type will fallback to strong, its not a digit for sure
    elif not strength.isdigit () and __has_english_characters(strength):
        print(
            "{}{}ERROR: Please specify the strength (low/medium/string) ar any given length like 4.{}".format(
                colors.BOLD, colors.FAIL, colors.ENDC
            )
        )
        return

    else:
        length = int(strength)

    # limit the length here
    if length < 4:

        print(
            "{}{}ERROR: Please generate a password with at least of length 4.{}".format(
                colors.BOLD, colors.FAIL, colors.ENDC
            )
        )
        return

    password = __generate_password(length)
    print(
        "{}{}GENERATED: Your password is '{}'{}".format(
            colors.BOLD, colors.OKGREEN, password, colors.ENDC
        )
    )
