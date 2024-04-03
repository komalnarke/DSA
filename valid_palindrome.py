str=" A man, a plan, a canal: Panama"
def palindrome(str):
    final = ''.join(filter(lambda x: x.isalnum(),str))

    return final == final[:-1]

print(palindrome(str))
