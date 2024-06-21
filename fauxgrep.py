import sys
import os
import re
import fileinput
from argparse import ArgumentParser

parser = ArgumentParser(description="Faux Grep")
# fauxgrep.py -i -n search-term file ...

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-n", dest="show_name", action="store_true", help="Print file name")
parser.add_argument("search_term", help="Search term")
parser.add_argument("files", nargs="*", help="File(s) to search")

args = parser.parse_args()

regex = re.compile(args.search_term, re.I if args.ignore_case else 0)

for raw_line in fileinput.input(args.files):
    if regex.search(raw_line):
        if args.show_name:
            print(fileinput.filename(), end=" ")
        print(raw_line.rstrip())