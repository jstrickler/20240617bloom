from electrical import *
from navigation import *

print(current())  # calls navigation.current(), not electrical.current()
print(voltage())
print(amps())
