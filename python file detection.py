#         Python file detection

import os

file_path = "test.txt"
if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("that is a file")
    elif os.path.isdir(file_path):
        print("that is a diractory")

else:
    print(f" the location {file_path} does not exists")

#exists(file.path) -> it is a boolean function to check if file exists or not
# or you can paste exact file path in folder or in desktop location like for example

# C:\Users\aakas\OneDrive\Desktop\python1 -> in folders

# C:\Users\aakas\OneDrive\Desktop   -> if it is in homepage 1.click on the file 2. go to properties 3.copy the file location