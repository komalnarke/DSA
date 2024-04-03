x = 121
def palin(x):
        new = str(x)
        res = new[::-1]
        if new == res:
            print("true")
        else:
            print("false")
print(palin(x))