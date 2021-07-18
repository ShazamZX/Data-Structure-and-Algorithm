#Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the numbers less than or equal to k together.(Sliding Window Technique)


def minswaps(arr,k):
    n = len(arr)
    #window size would be number of elements in array <= k
    window_size = 0
    for i in arr:
        if i<=k:
            window_size+=1
    #initializing swaps for 1st window
    swaps = 0
    for i in range(window_size):
        if arr[i]>k:
            swaps+=1
    res = swaps
    left = 0
    right = window_size

    while(right<n):
        if arr[left]>k:
            swaps-=1
        if arr[right]>k:
            swaps+=1
        res = min(res,swaps)
        left+=1
        right+=1
    
    return res

#driver code


arr = [2, 1, 5, 6, 3]
n = len(arr)
k = 3
print (minswaps(arr,k))
  
arr1 = [2, 7, 9, 5, 8, 7, 4]
n = len(arr1)
k = 5
print (minswaps(arr1,k))
         
