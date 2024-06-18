import sys

with open('DATA/mary.txt') as mary_in:
    print(f"{type(mary_in) = }")
    for raw_line in mary_in:  # mary_in.readline()
        line = raw_line.rstrip().upper()
        print(line)

sys.stdout.write("Hello, world\n")
# sys.stderr
# sys.stdin

print("We have a problem", file=sys.stderr)

