#check if an array has a any subarray whose sum is zero (Prefix sum method)


#the idea is that we calculate prefix sum at every index, if two prefix sum are same then the subarray between those two index have sum as zero

def subSum(arr):
    prefix_sum = set()
    prefix_sum_till_i = 0
    for i in range(len(arr)):
        prefix_sum_till_i+=arr[i]
        if prefix_sum_till_i == 0 or prefix_sum_till_i in prefix_sum:
            return True
        prefix_sum.add(prefix_sum_till_i)
    return False


#driver code

arr = [-3, 2, 3, 1, 6]
print(subSum(arr))

arr1 = [4, 2, -3, 1, 6]
print(subSum(arr1))
