from collections import Counter
nums = [1,1,4,5,7,4,5,8]
def duplicate(nums):
    counts = Counter(nums)
    result = [num for num , count in counts.items() if count>1 ]
    return result
print(duplicate(nums))