# rearrange an array with positive and negative in alternate places in O(1) space

def rearrange(arr):
    n = len(arr)
    i,j = 0,n-1

    while(i<=j):
        if arr[i]<0 and arr[j]>0:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        elif arr[i] >0 and arr[j]<0:
            i+=1
            j-=1
        elif arr[i]>0:
            i+=1
        elif arr[j]<0:
            j-=1
    
    if j==0 or i == n-1:
        return 

    j = 0
    while(j<n and i<n):
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j+=2

    
#driver code

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
rearrange(arr)
print(*arr)


