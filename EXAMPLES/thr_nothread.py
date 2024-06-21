import random
import time

def my_task(num):  # function to run in each thread
    time.sleep(random.randint(1, 3))
    print(f"Hello from my_task {num}")

for i in range(16):
    my_task(i)

print("Done.")  # "Done" is printed immediately -- the threads are "in the background"

