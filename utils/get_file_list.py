import os
import sys

'''
Gets a list of files in the Images folder of types bin, tar, and gz.
Returns them as a list.
'''

def get_file_list():
    try:
        dir_list = os.listdir('./Images')
    except FileNotFoundError:
        print("Images folder not found. Please create a folder named 'Images' \
in the script's root directory and place the images you wish to \
upload in this folder.")
        sys.exit(1)
    file_list = []
    acceptable_extensions = ('bin', 'tar', 'gz')
    for i in dir_list:
        if i.endswith(acceptable_extensions):
            file_list.append(i)
    if len(file_list) == 0:
        print("No acceptable images found. Please place images in the Images directory. \
Acceptable files are bin, tar, and gz.")
        sys.exit(1)
    else:
        return file_list
