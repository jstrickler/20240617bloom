from president import President

cities = list()

all_attributes = dir(cities)
print(f"{all_attributes = }\n")

p = President(1)
print(f"{dir(p) = }")

print(f"{p.birth_state = }")

print(f"{getattr(p, 'birth_state') = }")

x = object()

if hasattr(x, 'to_json'):
    to_json = getattr(x, 'to_json')
    to_json()
# else:
#     raise TypeError("Cannot convert object to JSON")

def full_name(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, 'full_name', property(full_name))

print(f"{p.full_name = }")

p2 = President(26)
print(f"{p2.full_name = }")








