#merge sort in O(1) Space
import math
def gap_calc(gap):
    if gap<=1:
        return 0
    return int(math.ceil(gap/2))
def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    gap = gap_calc(n+m)
    while(gap>0):
        i = 0
        while(i+gap<n):
            if arr1[i] > arr1[i+gap]:
               arr1[i],arr1[i+gap] = arr1[i+gap],arr1[i]
            i+=1
        j = gap-n if gap>n else 0
        while(i<n and j<m):
            if arr1[i] > arr2[j]:
               arr1[i],arr2[j] = arr2[j],arr1[i]
            i+=1
            j+=1
        if (j<m):
            j = 0
            while(j+gap<m):
                if arr1[j] > arr1[j+gap]:
                    arr1[j],arr1[j+gap] = arr1[j+gap],arr1[j]
                j+=1
        gap = gap_calc(gap)
    print(*arr1,end= " ")
    print(*arr2)


#driver method

a = [3, 5, 6, 8, 12]
b = [1, 4, 9, 13]
merge(a,b)
        

