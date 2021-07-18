"""
Given an array of positive integers. We need to make the given array a ‘Palindrome’. The only allowed operation is”merging” (of two adjacent elements). Merging two adjacent elements means replacing them with their sum. The task is to find the minimum number of merge operations required to make the given array a ‘Palindrome’.
To make any array a palindrome, we can simply apply merge operation n-1 times where n is the size of the array (because a single-element array is always palindromic, similar to single-character string). In that case, the size of array will be reduced to 1. But in this problem, we are asked to do it in the minimum number of operations.
"""




def minMerge(arr):
    ans = 0
    n = len(arr)
    l = 0
    r = n-1

    while(l<=r):
        if arr[l] == arr[r]:
            l+=1
            r-=1
        elif arr[l]<arr[r]:
            l+=1
            arr[l]+=arr[l-1]
            ans+=1
        else:
            r-=1
            arr[r]+=arr[r+1]
            ans+=1
    return ans

#driver code


arr = [1, 4, 5, 9, 1]
print(minMerge(arr))