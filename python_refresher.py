
x = 5      # create object with value 5 and type int, and assign object to name "x"
# bind "x" to obj
y = 10    

x = "Pastafazool"

# variable = object(value, type)
x = 9.5

m = x

print(m * 10)

thing = None


# literal data
#  "foo" 123  123.456 
# [x, y, z] {k:v, k:v} {x,y,z} (x, y, z)

# numeric types
#  int float bool complex

# sequence types
# str list tuple bytes

#  len(obj)  obj.count(value)  obj[start-at:stop-before:count-by] 
#  obj[index]  
#  for element in obj:
#      ...


# mapping types
# dict set

d = {}
d['NC'] = "Raleigh"
d['MN'] = "St. Paul"
d['SC'] = "Columbia"

for state, capital in d.items():
    print(state, capital)

print(f"{d['MN'] = }")

del d['SC']


states1 = ['NC', 'SC', 'MN', 'VA', 'WY']
states2 = ['MN', 'NC', 'CA', 'WV', 'AK', 'AL', 'AZ', 'AR']

s1 = set(states1)
s2 = set(states2)
print(f"{s1 & s2 = }")  # intersection
print(f"{s1 ^ s2 = }")  # xor
print(f"{s1 | s2 = }")  # union

x = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
x2 = set(x)
print(f"{x2 = }")

with open('DATA/breakfast.txt', "r") as breakfast_in:
    all_foods = breakfast_in.read().splitlines()  # split file into lines without \n

unique_foods = set(all_foods)
print(sorted(unique_foods, key=str.lower))

with open('unique_foods.txt', 'w') as foods_out:
    for food in sorted(unique_foods, key=str.lower):
        foods_out.write(food + "\n")

# color = input("Enter a color: ")
# print(f"You chose {color}")

color = 'pink'
if color not in ('teal', 'red', 'mauve', 'green', 'brown', 'tan', 'lavender'):
    print("I do not like that color!")

# if ...:
# elif ...:
# else:

# while ...:
#    ...

colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for color in colors:
    print(color.upper())
print()

x = [('a', 5), ('b', 10), ('c', 15)]
for thing in x:
    print(thing)
print()










