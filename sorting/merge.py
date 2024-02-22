from random import randint

def merge(nums: list[int]):
    if len(nums) < 2:
        return nums

    def merge_nums(first: list[int], second: list[int]):
        f = s = 0
        nf = len(first)
        ns = len(second)
        nums = []

        while f < nf and s < ns:
            if first[f] < second[s]:
                nums.append(first[f])
                f += 1
            else:
                nums.append(second[s])
                s += 1

        while f < nf:
            nums.append(first[f])
            f += 1

        while s < ns:
            nums.append(second[s])
            s += 1
        return nums

    mid = len(nums) // 2
    return merge_nums(merge(nums[:mid]), merge(nums[mid:]))

nums = [randint(0, 100) for _ in range(10)]
sorted_nums = merge(nums[:])

print(nums)
print(sorted_nums)
