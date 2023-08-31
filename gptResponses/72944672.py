# To copy the image files from the "A" folders to their parent folders and then remove the "A" and "B" folders, you can modify the code as follows:

# ```python
import shutil
import os

directory = "<Path to the parent directory>"
folders = os.listdir(directory)

for folder in folders:
    folder_path = os.path.join(directory, folder)
    if os.path.isdir(folder_path):
        a_folder_path = os.path.join(folder_path, "A")
        files = os.listdir(a_folder_path)
        for file in files:
            file_path = os.path.join(a_folder_path, file)
            shutil.copy2(file_path, folder_path)
        shutil.rmtree(a_folder_path)
        shutil.rmtree(os.path.join(folder_path, "B"))

print("\n ====> Images copied and folders removed successfully <====\n")
# ```

# Replace `<Path to the parent directory>` with the actual path to the directory containing the folders "301", "302", ..., "600".