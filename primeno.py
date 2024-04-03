n = 10

def prime(n):
    if n <= 1:
        return 0
    
    def prime(num):
        
        if num <=1:
            return False
        if num == 2:
            return True
        if num%2 == 0:
            return False
        
        for i in range(3, int(num**0.5)+1,2):
            if num%i == 0:
                return False
        return True
    
    count = 0
    for num in range(2,n):
        if prime(num):
            count +=1
    return count
    
print(prime(n))