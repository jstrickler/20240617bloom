
x = [1, 2, 3]
durham_latlon = 35.9940, 78.8986

print(f"{durham_latlon[0] = }")
print(f"{durham_latlon[1] = }")

lat, lon = durham_latlon  # unpack tuple to variables
print(f"{lat = }")
print(f"{lon = }")

# iterable -- object that can be looped over with a for loop

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', 'BASIC', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
]

for first_name, last_name, *product, dob in people:
    print(last_name, product)
print('-' * 60)

for *_, dob in people:
    print(dob)
print('-' * 60)

for person in people:
    print(person[-1])
print('-' * 60)

def spam(a, b):
    print(f"{a = }")
    print(f"{b = }")

spam(1, 2)
spam("hello", "world")

values = 8.3, 9.6

spam(values[0], values[1])
spam(*values)  #  spam(8.3, 9.6)

