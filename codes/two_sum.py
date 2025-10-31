import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums.sort()
target = 7

for i in range(len(nums)-1):
    random_i = random.choice(nums)

    for j in range(len(nums)-1):
        random_j = random.choice(nums)

        if random_i + random_j == target:
            arr = [random_i],[random_j]
            print(arr)
            break
    
