fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f0 = sorted(fruits)
print(f"{f0 = }\n")

f1 = sorted(fruits, key=str.lower)
print(f"{f1 = }\n")

f2 = sorted(fruits, key=len)
print(f"{f2 = }\n")

def by_len_name(item):
    return len(item), item.lower()

f3 = sorted(fruits, key=by_len_name)
print(f"{f3 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_month(person):
    year, month, day = person[3].split('-')
    month = int(month.lstrip('0'))
    year = int(year.lstrip('0'))
    return month, year

for person in sorted(people, key=by_month):
    print(person)
print()

def by_len_name(item):
    return len(item), item.lower()

f4 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print(f"{f4 = }\n")
print()

for person in sorted(people, key=lambda p: p[3]):
    print(person)


