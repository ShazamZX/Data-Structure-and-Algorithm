#The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#countAndSay(1) = "1"
#countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.


def func(n):
    if n == 1:
        return("1")
    if n == 2:
        return("11")
    s = "11"
    for i in range(2,n):
        t = ""
        s=s+"$"
        c = 1
        for j in range(1,len(s)):
            if s[j] == s[j-1]:
                c+=1
            else:
                t+= str(c)+s[j-1]
                c=1
        s=t
    return s


#driver code

print(func(4))
print(func(1))
print(func(2))
print(func(8))


