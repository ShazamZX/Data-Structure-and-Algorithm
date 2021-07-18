"""
Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.
"""


def partition(arr,range):
    n = len(arr)
    l,r = 0,n-1
    i = 0
    while(i<r):
        if arr[i]>range[1]:
            arr[i], arr[r] = arr[r],arr[i]
            r-=1
        elif arr[i]<range[0]:
            arr[i], arr[l] = arr[l],arr[i]
            l+=1
            i+=1
        else:
            i+=1

#driver code

arr = [1, 14, 5, 20, 4, 2, 54,
           20, 87, 98, 3, 1, 32]

 
partition(arr,(10, 20))
print(*arr)

