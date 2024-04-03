candidates = [2,3,6,7]
target = 7
def combination(candidates,target):
    res = []
    for i in range (len(candidates)):
        for j in range(i+1, len(candidates)):
            if candidates[i] + candidates[j]==target:
                res.append([candidates[i],candidates[j]])
        return res
print(combination(candidates,target))