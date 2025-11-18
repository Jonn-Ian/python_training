import random

# generate a random numbers from 0 to 100
random_numbers = []
for i in range(100):
    random_numbers.append(random.randint(0, 100))

def bubble_sort():
    for i in range(len(random_numbers)):
