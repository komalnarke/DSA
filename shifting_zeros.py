nums = [0,1,0,3,12]

def shift(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right]!=0:
            nums[right] , nums[left] = nums[left] , nums[right]
            left += 1
    return nums
print(shift(nums))