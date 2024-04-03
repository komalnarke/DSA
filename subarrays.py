nums = [1, 3, 5, 2, 7, 5]
mink = 1
maxk = 5

def subarray(nums, mink, maxk):
    res = 0
    start = -1
    for i in range(len(nums)):
        if nums[i] >= mink and nums[i] <= maxk:
            if start == -1:
                start = i
        else:
            start = -1
        if start != -1:
            res += i - start + 1
    return res

print(subarray(nums, mink, maxk))

