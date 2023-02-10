# [WIP]
import os
import wave

from plzz.helper_functions.helper_functions import colors
from plzz.helper_functions.snippets import __pathname_checker


def __move_audio_files(file):
    """
    Moves audio files in a directory based on bitrate.

    Parameters:
    pathname: path to a file.

    Returns:
    None

    Raises:
    FileNotFoundError: If the directory does not exist.
    ValueError: If the low or high bitrate thresholds are not positive integers, or the high bitrate threshold is less than the low bitrate threshold.
    """

    if file.endswith(".wav") or file.endswith(".mp3"):
        # Open the audio file
        with wave.open(file, "rb") as f:
            # Get the bitrate
            bitrate = f.getframerate()

            # # Determine the destination directory
            # if bitrate < low_bitrate:
            #     dest_dir = "low_bitrate"
            # elif bitrate > high_bitrate:
            #     dest_dir = "high_bitrate"
            # else:
            dest_dir = str(bitrate)

            # Create the destination directory if it doesn't exist
            # get the base directory name from the filename
            basename = os.path.dirname(file)

            if not os.path.exists(os.path.join(basename, dest_dir)):
                os.makedirs(os.path.join(basename, dest_dir))

            # Move the file to the destination directory
            os.rename(file, os.path.join(basename, dest_dir, file))
            print("{}{}BITRATE: '{}' moved to folder {}{}".format(
                colors.BOLD,
                colors.OKGREEN,
                file,
                bitrate,
                colors.ENDC
            ))
    else:
        print(
            "{}{}ERROR: '{}' is not supported!{}".format(
                colors.BOLD, colors.FAIL, file, colors.ENDC
            )
        )


def move_audio_by_bitrate(pathname: str):
    """Organize audio files based on their bitrate.

    Args:
        pathname (str): A audio file or a folder containing audio files.
    """
    files = __pathname_checker(pathname)
    for _file in files:
        __move_audio_files(_file)
