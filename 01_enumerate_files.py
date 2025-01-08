# Q) enumerate files in a directory

# solution: https://www.geeksforgeeks.org/python-list-files-in-a-directory/

import os

DIR_PATH = '/workspaces/practice_python/01_test_directory'

# method1: 
def list_files_using_listdir(directory):
    entries = os.listdir(directory)
    files_in_same_dir = [file for file in entries if os.path.isfile(os.path.join(directory, file))] #filter files
    return files_in_same_dir



# method2
def list_files_using_walk(directory):
    file_list = []
    for (root,dirs,files) in os.walk(directory):
        for file in files:
            file_list.append(file)
    return file_list


# Example usage:
dir_files = list_files_using_listdir(DIR_PATH)
all_files = list_files_using_walk(DIR_PATH)
print(dir_files, all_files)



