#check whether string is palindrome or not
def palin(s):
    return (s == s[::-1])

#driver code


print(palin("madam"))
print(palin("jonathan"))