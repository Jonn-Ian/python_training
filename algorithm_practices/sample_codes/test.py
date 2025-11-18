import random

random_numbers = []
target = 20

for i in range(100):
    random_numbers.append(random.randint(1, 100))

for j in range(len(random_numbers)):
    
    if target == random_numbers[j]:
        print(target, random_numbers[j])
