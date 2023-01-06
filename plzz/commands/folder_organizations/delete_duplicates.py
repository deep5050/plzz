import os
import hashlib

from plzz.helper_functions.helper_functions import colors



def delete_duplicate_files(directory):
    """Generates the MD5 hash of all the files in a given directory and deletes one of the files if two hashes match.
    
    Args:
        directory (str): The directory path.
    
    Raises:
        OSError: If the directory does not exist.
        ValueError: If the directory path is empty.
    """
    if not directory:
        raise ValueError("Directory path cannot be empty.")
    if not os.path.exists(directory):
            print(
            "{}{}ERROR: Directory '{}' does not exist!{}".format(
                colors.BOLD, colors.FAIL, directory, colors.ENDC
            ))
            return
        # raise OSError(f"Directory '{directory}' does not exist.")
    
    # Create a dictionary to store the hashes of the files
    hash_dict = {}
    count = 0
    # Iterate through all the files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Generate the MD5 hash of the file
        hash_value = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        
        # If the hash value is not in the dictionary, add it
        if hash_value not in hash_dict:
            hash_dict[hash_value] = file_path
        # If the hash value is already in the dictionary, delete one of the files
        else:
            os.remove(file_path)
            count += 1
            print(
            "{}{}Removing-> '{}' {}".format(
                colors.BOLD, colors.OKGREEN, file_path, colors.ENDC
            )
        )
    if count == 0:
        print(
            "{}{}INFO: No duplicate files present {}".format(
                colors.BOLD, colors.OKBLUE, colors.ENDC
            )
        )

