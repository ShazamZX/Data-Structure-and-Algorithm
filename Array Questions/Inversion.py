#Given an array of integers. Find the Inversion Count in the array. Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.


def sort(arr,temp,left,right):
    count = 0
    if left<right:
        mid = (left+right)//2
        #left subtree
        count+= sort(arr,temp,left,mid)
        #right subtree
        count+=sort(arr,temp,mid+1,right)
        count+=merge(arr,temp,left,mid,right)
    return count

def merge(arr,temp,left,mid,right):
    i = left
    j = mid+1
    count = 0
    k = left

    while(i<=mid and j<=right):
        if arr[i]<=arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            #inversions occur when elements are taken from right subtree
            count+=(mid-i+1) #if arr[j] is smaller than a[i] then its also smaller than all other subsequent elements in left subtree
            j+=1
        k+=1
    while(i<=mid):
        temp[k] = arr[i]
        i+=1
    while(j<=right):
        temp[k] = arr[j]
        j+=1
    for pos in range(left,right+1):
        arr[pos] = temp[pos]

    return count

def merge_sort(arr,n):
    temp = [None]*n
    return sort(arr,temp,0,n-1)


#driver code


arr = [3,1,2]
n = len(arr)
result = merge_sort(arr, n)
print("Number of inversions are", result)
    
        