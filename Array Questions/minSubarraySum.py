#Find subarray with given sum with negatives allowed in constant space

def subarrsum(arr,target):
    if target in arr:
        return [target] 
    n = len(arr)
    minval = min(arr)
    l = 0
    res = arr[0] + abs(minval)
    for r in range(1,n+1):
        while(res-(r-l)*abs(minval)>target and l<r):
            res = res - (arr[l] + abs(minval))
            l+=1
        if (res-(r-l)*abs(minval)==target):
            return arr[l:r]
        if(r<n):
            res = res + (arr[r] + abs(minval))
    return [-1]



#driver code

arr = [10, -12, 2, -2, -20, 10]

print(subarrsum(arr,-2))

            