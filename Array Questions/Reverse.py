#Reverse the array

def rev(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    print(*arr) 

#Driver

arr = list(map(int,input().split()))
rev(arr)