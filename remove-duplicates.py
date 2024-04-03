from collections import Counter
nums = [1,1,1,2,2,3]

def remove(nums):
    if not nums:
        return 0
    
    k = 0
    
    for num in nums:
        if k>2 or num>nums[k-2]:
           nums[k]= num 
           k+= 1
           
    return k and (nums[:k])
           