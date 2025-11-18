import random

# generate a random numbers from 0 to 100
random_numbers = []
for i in range(100):
    random_numbers.append(random.randint(1, 100))

# sort the list of random numbers
random_numbers.sort()

def binary_search(target):
    low = 0
    high = len(random_numbers) - 1

    while low <= high:
        # iterate while the middle isn't found
        middle = (low + high) // 2

        # check if the target is equal to the middle element while iterating the division
        if target == random_numbers[middle]:
            print("taget found: ", random_numbers[middle], target)
            return
        
        # if the target is less than the middle element, search in the left half
        elif target < random_numbers[middle]:
            high = middle -1
            
        # else if the target is higher than the middle, search for the higher elements
        else:
            low = middle +1
    
    # if the target doesn't exist in the list
    print("target doesn't exist")

input = int(input("Enter a number to search (1-100): "))
print("\n", random_numbers)
binary_search(input)