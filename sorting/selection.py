from random import randint

def selection(nums: list[int]):
    for i in range(len(nums)):
        i_min = i
        for j in range(i+1, len(nums)):
            if nums[i_min] > nums[j]:
                i_min = j
        nums[i], nums[i_min] = nums[i_min], nums[i]
    return nums

nums = [randint(0, 100) for _ in range(10)]
sorted_nums = selection(nums[:])

print(nums)
print(sorted_nums)
