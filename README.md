 <div align=center>
<h1 align=center> PLZZ ("please")</h1>

<img align=center src="logo.jpg" alt="logo">

<p align=center> A python CLI to automate daily tasks of both common and advanced users :) </p>

</div>


![About](about.svg.svg)

# Install

```bash
 pip3 install plzz-cli
 ```

# Run

Run the app with command **`plzz`**


<!-- ![Install](install.svg.svg) -->


# List of commands

**`plzz --develop`** : Only for development purpose. Not intended to ship during publishing.

**`plzz --about`** : About the app.

**`plzz --list-commands`** : List all the supported operations.

**`plzz --update`** : Check for if any update of the app is available.

**`plzz --find-commands`** : Search for a operations.

**`plzz [OPERATION]`** : Run a operation from the supported list. Ex. `plzz create-random-text-files`



# Supported operations

## FILE OPERATIONS

**create-random-text-files** : Creates a specified number of random text files with random text under a given directory.

**create-lorem-ipsum-file** : Creates a Lorem Ipsum file with a specified number of lines.

**generate-toc** : Generate Table of contents from a given markdown file or all the markdown files under a directory.

**format-sentences** : Format each sentences correctly in a english text a file or all files under a directory.

**find-urls** : Find all the links from a text file or all the text files under a directory.

**count-offensive-words** : Count offensive words from a file or a directory.

**censor-offensive-words** : Censor offensive words from a file or all files under a directory.

**check-hash** : Encrypt a file (MD5) or all the files under a directory and print the key(s).

**count-word** : Count number of words in a file or under all the files under a given directory.

## FOLDER ORGANIZATIONS

**add-missing-extensions** : Add missing extension to a file or all the files under a directory.

**delete-duplicates** : Generates the MD5 hash of all the files in a given directory and deletes one of the files if two hashes match.

**rename-files** : Rename a file/all files under directory by replacing specified character with new one.

**delete-empty-files** : Delete all empty text files from src_dir.

**replace-words** : Replace all the words in a given file or all the files under a directory with a new word.

## UTILITIES

**download-todays-wallpaper** : Download today's wallpaper from bing, and save them.

**generate-password** : Generate a password of a given strength (low,medium,strong) or any specific length.

**create-qr-code** : Create qr code and save it as a image.

## DEVELOPMENT TASKS

**upload-to-gist** : Upload a file or all files under a directory to Github Gist.

**add-license** : Create a license file of desired type.


# Changes

See the [CHANGELOG](CHANGELOG) file for more details.


# Support

<p align=center><a href="https://www.buymeacoffee.com/deep5050" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 117px !important;" ></a></p>