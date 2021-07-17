#find a pair of number in an array which has a given sum
def pair(nums,target):
    d = set()
    res = []
    for num in nums:
        k = target-num
        if k in d:
            res.append((num,k))
        
        else:
            d.add(num)
    return res
    
#driver code
arr = [10, 12, 10, 15, -1, 7, 6, 
                   5, 4, 2, 1, 1, 1]
sum = 11

print(*pair(arr,sum))
