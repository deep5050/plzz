import qrcode
import os

from plzz.helper_functions.helper_functions import colors


def __create_qr(data, filename, color="black", bgcolor="white"):

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=5,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color=bgcolor)
        img.save(filename)
        return 1



def create_qr_code(data:str, filename: str,color="black",bgcolor="white"):
    """Create qr code and save it as a image.

    Args:
        filename (str): Image name to be saved as.
    """
    if os.path.exists(filename):
        print(
            "{}{}ERROR: File '{}' already exists! {}".format(
                colors.BOLD, colors.FAIL, filename, colors.ENDC
            )
        )
        return
    if data.strip == "":
        print("{}{}ERROR: No data given!{}".format(
            colors.BOLD,
            colors.FAIL,
            colors.ENDC
        ))
        return
    return_code = __create_qr(data=data,filename=filename,color=color,bgcolor=bgcolor)
    if return_code != 0:
        print("{}{}GENERATED: QR code generated as '{}'{}".format(
            colors.BOLD,
            colors.OKGREEN,
            filename,
            colors.ENDC
        ))
    else:
        print("{}{}ERROR: Something went wrong!{}".format(
            colors.BOLD,
            colors.FAIL,
            colors.ENDC
        ))

