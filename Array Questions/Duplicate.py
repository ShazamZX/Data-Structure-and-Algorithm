# Find duplicate number in N+1 intergers array

arr = list(map(int, input().split()))
N = len(arr)-1
print(sum(arr) - (N*(N+1)//2))