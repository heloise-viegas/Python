#list all files in the folders

import os

def list_files(folder):
    try:
        files = os.listdir(folder)
        return files,None
    except FileNotFoundError:
        return None,FileNotFoundError
    except PermissionError:
        return None,FileNotFoundError


def main():
    folders = input("Specify folders with spaces inbetween.").split()
    for folder in folders:
        files, error=list_files(folder)
        if files:
            print("Files in folder " + folder)
            for file in files:
                print(file)
        else:
            print("Error in "+ folder +": "+ error)
            
