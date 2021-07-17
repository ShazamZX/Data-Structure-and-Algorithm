#Find minimum jumps req to reach end of array
import sys
def minJump(arr,n):
    dp = [None]*n
    dp[n-1] = 0
    for i in range(len(dp)-2,-1,-1):
        steps = arr[i]
        min = sys.maxsize
        for j in range(1,steps+1):
            if i+j<n:
                if dp[i+j] is not None and dp[i+j]<min:
                    min = dp[i+j]
        if min!= sys.maxsize:
            dp[i] = min+1
    return dp[0]

# driver code


N = 11 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJump(arr,N))