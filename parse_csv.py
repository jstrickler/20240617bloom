import csv

with open('DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in)
    for row in rdr:
        print(f"{row[1]} {row[0]}")
