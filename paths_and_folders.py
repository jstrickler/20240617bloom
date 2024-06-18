import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"{file_path = }")

print(f"{os.path.basename(file_path) = }")
print(f"{os.path.dirname(file_path) = }")
print(f"{os.path.abspath(file_path) = }")

print(f"{os.path.getsize(file_path) = }")

raw_timestamp = os.path.getmtime(file_path)
print(f"{raw_timestamp = }")

file_mod_time = datetime.fromtimestamp(raw_timestamp)
print(f"{file_mod_time = }")
print(file_mod_time)
print(f"{os.path.isdir(file_path) = }")
print(f"{os.path.isfile(file_path) = }")
print(f"{os.path.isabs(file_path) = }")

for path in 'DATA/alice.txt', 'DATA/Bloomington.txt':
    print(path, os.path.exists(path))

MIN_FILE_SIZE = 10000

for folder, folders, file_names in os.walk('.'):
    if '.git' in folders:
        folders.remove('.git')
    print(folder)
    for file_name in file_names:
        # does file name end with .py??
        file_path = os.path.join(folder, file_name)
        file_size = os.path.getsize(file_path)
        if file_size > MIN_FILE_SIZE:
            file_timestamp = os.path.getmtime(file_path)
            file_modtime = datetime.fromtimestamp(file_timestamp)
            print(f"    {file_size:9d} {file_modtime:%x} {file_name}")            

