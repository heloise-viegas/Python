#list all files in the folders

import os

def list_files(folder):
    try:
        files = os.listdir(folder)
        return files,None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"


def main():
    folders = input("Specify folders with spaces in between.").split()
    for folder in folders:
        files, error=list_files(folder)
        if files:
            print("=========Files in folder " + folder+"=========")
            for file in files:
                print(file)
        else:
            print("Error in "+ folder +": "+ error)
            
if __name__ == "__main__":
    main()