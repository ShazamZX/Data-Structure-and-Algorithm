#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.(CLASSIC TWO POINTER PROBLEM)

def watertrapped(arr):
    n = len(arr)
    l = 0
    r = n-1
    l_bound = 0
    r_bound = 0
    res = 0
    while(l<=r):
        if(arr[l]<arr[r]):
            if l_bound<arr[l]:
                l_bound = arr[l]
            else:
                res+= l_bound-arr[l]
            l+=1
        else:
            if r_bound<arr[r]:
                r_bound = arr[r]
            else:
                res+= r_bound-arr[r]
            r-=1
    return res


#driver code

arr1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(watertrapped(arr1))
arr2 = [3,0,4,1,0,2,5,5,1,0,4]
print(watertrapped(arr2))

