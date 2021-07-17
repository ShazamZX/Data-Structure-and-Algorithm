#find Largest sum contiguous Subarray [V. IMP] - Kadane's Algo

def maxSubArraySum(a):
        max = -(10**7)-1
        max_till_i = 0
        start = -1
        end = -1
        for i in range(len(a)):
            max_till_i+=a[i]
            if max_till_i > max:
                max = max_till_i
                start = end
                end = i
            if max_till_i < 0:
                max_till_i = 0
            
        print(f"Max sum is {max} in the range {start} to {end}")

#Driver Code

arr = list(map(int,input().split()))
maxSubArraySum(arr)