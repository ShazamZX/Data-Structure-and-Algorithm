#Kth Max and KthMin of an Array
def KMinMax(arr,k):
    arr = sorted(arr)
    print("Min",arr[k-1])
    print("Max",arr[len(arr)-k])


#Driver code
k = int(input())
arr = list(map(int,input().split()))
if k<len(arr):
    KMinMax(arr,k)