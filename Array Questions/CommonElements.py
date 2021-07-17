#find common elements in 3 arrays

def common(a,b,c):
    a = set(a)
    b = set(b)
    c = set(c)
    common = list((a.intersection(b)).intersection(c))
    return common


#driver code
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(*common(ar1,ar2,ar3))
