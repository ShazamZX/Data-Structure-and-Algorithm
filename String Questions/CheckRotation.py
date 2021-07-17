#check if one string is rotation of another

def isRotation(s1,s2):
    if len(s1)!=len(s2): return False
    return ((s1+s1).count(s2)>0)



#driver code

s1 = "ABCDE"
s2 = "DEABC"
print(isRotation(s1,s2))