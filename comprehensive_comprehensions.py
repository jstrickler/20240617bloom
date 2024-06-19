fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f[:3].title()
    f0.append(f)

#    [VALUE for VAR in ITERABLE]
f1 = [f[:3].title() for f in fruits]
print(f"{f1 = }\n")

f2 = ["".join(reversed(f)) for f in fruits]
print(f"{f2 = }\n")

f3 = [f.upper() for f in fruits]
print(f"{f3 = }\n")

fruit_gen = (f.upper() for f in fruits)
print(f"{fruit_gen = }")

for fruit in fruit_gen:  # iterating over a virtual list of fruits
    print(fruit)
print()

