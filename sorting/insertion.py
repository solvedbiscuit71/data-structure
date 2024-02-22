from random import randint

def insertion(nums: list[int]):
    for i in range(1, len(nums)):
        for j in range(i-1, -1, -1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            else:
                break
    return nums

nums = [randint(0, 100) for _ in range(10)]
sorted_nums = insertion(nums[:])

print(nums)
print(sorted_nums)
