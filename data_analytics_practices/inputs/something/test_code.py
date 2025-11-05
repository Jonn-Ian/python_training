nums = [2, 3, 4, 4, 1]
nums.sort()

for i in range(len(nums)-1):
    if nums[i] == nums[i + 1]:
        arr = [nums[i]],[nums[i + 1]]
        print(True, arr)
        break
    else:
        print(False)