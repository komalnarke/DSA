from collections import Counter
nums = [1,1,1,4,5,4,4,4,6,6]
def majority(nums):
    counts = Counter(nums)
    return counts.most_common(1)[0][0]
print(majority(nums))