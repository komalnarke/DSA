nums = [10, 12, 13]

def encrypt(nums):
    def en(x):
        
        largest_num = max(map(int,str(x)))
        return int(str(largest_num)*len(str(x)))
    encrypt_num = map(en,nums)
    return sum(encrypt_num)
print(encrypt(nums))