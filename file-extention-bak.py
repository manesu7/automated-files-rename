import os

# Specify the directory path
folder_path = "folder-txt-files"

# Loop through all files in the directory
for filename in os.listdir(folder_path):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        old_file = os.path.join(folder_path, filename)
        
        # Verify it's a file and not a directory
        if os.path.isfile(old_file):
            new_file = old_file + ".bak"
            os.rename(old_file, new_file)
