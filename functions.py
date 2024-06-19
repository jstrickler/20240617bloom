import os
import sys

def add(x, y):
    return x + y

result = add(5, 8)
print(f"{result = }")

def junk():
    pass  # does nothing

j = junk()
print(f"{j = }")

# void function
def remove_files_by_extension(folder, extension):
    for file_name in os.listdir(folder):
        if file_name.endswith(extension):
            file_path = os.path.join(folder, file_name)
            os.remove(file_path)

remove_files_by_extension('.', '.bak')
# remove_files_by_extension('.foo', 'DATA')  # invalid
remove_files_by_extension(extension='.foo', folder='DATA')  # invalid

def delete_them(*file_paths):
    for file_path in file_paths:
        print(f"I would delete {file_path}")

delete_them('DATA/alice.txt')
delete_them('DATA/mary.txt', 'ANSWERS/c2f.py')
delete_them()

#   my_function(pos1, pos2, *opt, named1, named2):
#   my_function(pos1, pos2, *, named1, named2):

def pygrep(search_term, *file_paths, ignore_case=False):
    all_lines = []
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if ignore_case:
                    search_line = line.lower()
                else:
                    search_line = line
                if search_term in search_line:
                    element = file_path, line.rstrip()
                    all_lines.append(element)
    return all_lines

results = pygrep('lizard', 'DATA/alice.txt', 'DATA/words.txt')
for file_path, line in results:
    print(f"{file_path:20} {line}")
print()

results = pygrep('lizard', 'DATA/alice.txt', 'DATA/words.txt', ignore_case=True)
for file_path, line in results:
    print(f"{file_path:20} {line}")
print()

# local nonlocal global builtin

x = 5

print(x)

def eggs():
    xx = 47
    def spam():
        # x = "harmony"
        print(x)
    return spam

def print(*args):
    sys.stdout.write("HA HA HA\n")
    for arg in args:
        sys.stdout.write(str(arg) + ' ')
    sys.stdout.write('\n')

s = eggs()
print(f"{type(s) = }")
s()  # calling spam()

print("What is happening?")
