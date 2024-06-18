
# str -- decoded characters
# bytes -- encoded characters  (text from DB or network)
#       -- raw data (anything else)

t = "apple"

s1 = "75\u00B0"
print(f"{s1 = }")

# Unicode -- mapping of characters to numbers
# utf-8  -- encoding of numbers 
b1 = s1.encode()  #   chr -> unicode
print(f"{b1 = }")

s2 = b1.decode()
print(f"{s2 = }")

