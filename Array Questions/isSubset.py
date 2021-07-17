# check whether one array is subset of another(B subset of A?)


def subset(A,B):
    if (A == A.union(B)):
        return True
    return False

#driver code

A = set([1,2,4,2,1,3,5,6])
B = set([1,5,3,6,7])
print(subset(A,B))
