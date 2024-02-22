def heapsort(nums: list[int]):
    n = len(nums)
    for i in range(n//2 - 1, -1, -1):
        bubble_down(nums, n, i)
    while n > 0:
        nums[n-1], nums[0] = nums[0], nums[n-1]
        bubble_down(nums, n-1, 0)
        n = n-1

def max_child(tree, n, i):
    l = 2*i + 1 if 2*i + 1 < n else None
    r = 2*i + 2 if 2*i + 2 < n else None
    if l and r:
        return r if tree[r] > tree[l] else l
    return l

def bubble_down(tree, n, i):
    j = max_child(tree, n, i)
    while j and tree[j] > tree[i]:
        tree[i], tree[j] = tree[j], tree[i]
        i = j
        j = max_child(tree, n, i)
