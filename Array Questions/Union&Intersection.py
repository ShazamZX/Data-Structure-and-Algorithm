#Find the Union and Intersection of the two sorted arrays.

def NumberofElementsInIntersection(a,b):
        return len(list(set(a).intersection(set(b))))
def NumberofElementsInUnion(a,b):
        return len(list(set(a).union(set(b))))

#Driver Code

a = list(map(int,input().split()))
b = list(map(int,input().split()))

print("Intersection",NumberofElementsInIntersection(a,b))
print("Union",NumberofElementsInUnion(a,b))
