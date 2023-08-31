# ```python
import unittest
import os

def myFunc(root_dir):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".iso"):
                # Construct the new file path
                old_file_path = os.path.join(foldername, filename)
                new_file_path = os.path.join(foldername, "game.iso")

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")

class TestMyFunc(unittest.TestCase):

    def test_rename_files(self):
        # Create test directories and files
        root_dir = "test_dir"
        subfolders = ["folder1", "folder2", "folder3"]
        files = ["file1.iso", "file2.iso", "file3.txt"]
        expected_files = ["game.iso", "game.iso", "file3.txt"]
        os.makedirs(root_dir)
        for subfolder in subfolders:
            os.makedirs(os.path.join(root_dir, subfolder))
            for file in files:
                open(os.path.join(root_dir, subfolder, file), "w").close()
        
        # Rename files using myFunc
        myFunc(root_dir)
        
        # Check if files are renamed correctly
        for i, subfolder in enumerate(subfolders):
            subdir = os.path.join(root_dir, subfolder)
            for file in os.listdir(subdir):
                self.assertEqual(file, expected_files[i])
        
        # Clean up test directories and files
        for subfolder in subfolders:
            subdir = os.path.join(root_dir, subfolder)
            for file in os.listdir(subdir):
                os.remove(os.path.join(subdir, file))
            os.rmdir(subdir)
        os.rmdir(root_dir)

if __name__ == "__main__":
    unittest.main()
# ```
# ```