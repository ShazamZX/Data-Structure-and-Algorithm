#Move all the negative elements to one side of the array 
from collections import Counter

def sort012(arr):
    count = dict(Counter(arr))
    res = [None]*len(arr)
    i = 0
    while(count[0]>0):
        res[i] = 0
        count[0]-=1
        i+=1
             
    while(count[1]>0):
        res[i] = 1
        count[1]-=1
        i+=1
                
    while(count[2]>0):
        res[i] = 2
        count[2]-=1
        i+=1
        
    return res
arr = list(map(int,input().split()))
print(*sort012(arr))