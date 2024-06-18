import os

print(f"{os.environ.get('HOME') = }")
print(f"{os.environ.get('LOGNAME') = }")

# set environment values
os.environ['BREAKFAST'] = "waffles"

path_info = os.environ['PATH']
print(path_info)
