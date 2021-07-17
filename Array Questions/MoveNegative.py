#Move all the negative elements to one side of the array 

def move(arr):
    j = 0 #counter for -ve ele
    for i in range(len(arr)):
        if arr[i]< 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr

#driver code
arr = list(map(int,input().split(',')))
arr = move(arr)
print(*arr)