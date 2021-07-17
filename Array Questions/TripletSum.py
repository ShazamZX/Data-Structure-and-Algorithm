#find the triplet in an array with a target sum (Two Pointer Method)


def triplet(arr,target):
    arr.sort()
    n = len(arr)
    res = []
    for i in range(n-2):
        l = i+1
        r = n-1
        while(l < r):
            if (arr[i] + arr[l] + arr[r] == target):
                res.append((arr[l],arr[i],arr[r]))
                r-=1
                l+=1
            elif(arr[i] + arr[l] + arr[r] > target):
                r-=1
            else:
                l+=1
    return res

#driver code

arr = [1, 4, 45, 6, 10, 8, 9, 3, 3]
print(*triplet(arr,22))


                