#os.path.exists()
#
# import os
#
# file_name ="E:/coding/Python-Programming/File Handling/practice.txt"
#
# if os.path.exists(file_name):
#     print("File Exists")
# else:print("File did not exists")


#pathlib.Path.exists()

from pathlib import Path

file_name = Path("E:/coding/Python-Programming/File Handling/practice.txt")

if file_name.exists:
    print("File Exists")
else:print("File did not exists")
