#find the length of the longest subsequence having consecutive numbers 

def subseq(arr):
    arr = list(set(sorted(arr)))
    maxlen = 0
    len_till_i = 1
    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]-1:
            len_till_i+=1
        else:
            maxlen = max(maxlen,len_till_i)
            len_till_i = 1

    return maxlen


#driver code

arr = [1, 9, 3, 10, 4, 20, 2, 30]
print(subseq(arr))
