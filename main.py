import os

def remove_empty_folders(path):
    removed_folders = []
    # Iterate over all the directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        try:
            # If a directory is empty
            if not os.listdir(dirpath):
                # Remove the empty directory
                os.rmdir(dirpath)
                removed_folders.append(dirpath)
        except PermissionError:
            print(f"Permission denied: {dirpath}")
    
    # Print the removed folders
    for folder in removed_folders:
        print(f"Removed empty folder: {folder}")

# Specify the path to the directory where you want to remove empty folders
directory_path = r"C:\Users"

# Call the function to remove empty folders
remove_empty_folders(directory_path)
