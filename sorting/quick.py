from random import randint

def quick(nums: list[int]):
    if len(nums) < 2:
        return nums

    def partition():
        i = 0
        for j in range(1, len(nums)):
            if nums[j] < nums[0]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
        nums[0], nums[i] = nums[i], nums[0]
        return i

    k = partition()
    return quick(nums[:k]) + [nums[k]] + quick(nums[k+1:])


nums = [randint(0, 100) for _ in range(10)]
sorted_nums = quick(nums[:])

print(nums)
print(sorted_nums)
