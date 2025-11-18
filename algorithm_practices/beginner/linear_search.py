import random

# linear search algorithm
def linear_search(target):
    for index in range(len(random_numbers)):
        if target == random_numbers[index]:
            print(target, random_numbers[index])

# generate random numbers
random_numbers = []
for i in range(100):
    random_numbers.append(random.randint(1, 100))

# target from user
input = int(input("enter a number to search: "))


print(random_numbers)
# perform
linear_search(input)
