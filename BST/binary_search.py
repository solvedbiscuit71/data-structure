def lower(nums: list[int], key):
    i = 0
    jump = len(nums) // 2
    while jump > 0 and nums[i] != key:
        if i + jump < len(nums) and nums[i+jump] <= key:
            i += jump
        else:
            jump //= 2
    return i if i > 0 or nums[i] == key else -1

def upper(nums: list[int], key):
    i = len(nums) - 1
    jump = len(nums) // 2
    while jump > 0 and nums[i] != key:
        if i - jump >= 0 and nums[i-jump] >= key:
            i -= jump
        else:
            jump //= 2
    return i if i < len(nums) - 1 or nums[i] == key else len(nums)

def search(nums: list[int], key):
    return lower(nums, key) == upper(nums, key)
