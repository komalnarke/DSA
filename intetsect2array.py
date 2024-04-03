# for equal number of lengths of array
nums1 = [1,2,2,1]
nums2 = [2,2,1,3]
def intersection(nums1 , nums2):
    res = []
    for i in nums1:
        for j in nums2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                return res
print(intersection(nums1,nums2))

#for different length of array
num1 = [1,2,2,1]
num2 = [2,2]
def intersection (num1 , num2):
    set1 = set(num1)
    set2 = set(num2)
    res = set1.intersection(set2)
    return list(res)
print(intersection(num1, num2))