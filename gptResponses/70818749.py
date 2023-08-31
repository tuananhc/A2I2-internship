# To achieve this, you can use the `os` module in Python to navigate through the folders and rename the files. Here's an example script that you can adapt to your specific folder structure:

# ```python
import os

# Root folder containing the subfolders
root_folder = "../test_dir"
print(1)
# Function to rename files
def rename_files(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        print(foldername)
        for filename in filenames:
            if filename.endswith(".iso"):
                print(filename)
                # Construct the new file path
                old_file_path = os.path.join(foldername, filename)
                new_file_path = os.path.join(foldername, "game.iso")

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")

# Call the function
rename_files(root_folder)
# ```

# Make sure to replace `/path/to/root_folder` with the actual path to your root folder containing the subfolders. This script will recursively go through all subfolders within the root folder, check if there's a file ending with ".iso", and rename it to "game.iso".

# Note: Before running this script, it's always a good idea to test it on a backup of your files or a small subset of them, just to be safe.