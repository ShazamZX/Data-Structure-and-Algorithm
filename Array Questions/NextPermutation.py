def nextperm(arr):
    n = len(arr)
    if n==1:
        return arr
    i = 0
    j = 0
    for i in range(n-1,0,-1):
        if arr[i-1]<arr[i]:
            break
    if i==0:
        return arr[::-1]
    else:
        prev = i
        for j in range(n-1,i-1,-1):
            if arr[i-1] < arr[j] and arr[j]<arr[prev]:
                prev=j
    arr[i-1],arr[prev] = arr[prev],arr[i-1]
    arr = arr[:i] + arr[i:][::-1]
    return arr

# driver code

print(nextperm([1,1,1,2]))