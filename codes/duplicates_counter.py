nums = [2, 1, 224, 4, 534, 32 ,5 ,145 ,3, 23, 4]
nums.sort() #sort this numerically from 1 to the end

print(nums)
for i in range(len(nums) - 1):
    arr = [nums[i]], nums[i + 1]
    print(arr)
    if nums[i] == nums[i + 1]:
        print(nums[i], [i])
        print(True)
        break