# find the elements in an array which occur n/k times where n = length
from collections import Counter
def occur(arr,k):
    res = []
    threshold = len(arr)//k
    element_count = Counter(arr)
    for num in element_count:
        if element_count[num]>threshold:
            res.append(num)

    return res 

#driver code

arr = [3, 1, 2, 2, 1, 2, 3, 3]
print(*occur(arr,4))
