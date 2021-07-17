#to print duplicate characters in string
from collections import defaultdict
def duplicate(s):
    res = []
    count = defaultdict(int)
    for i in s:
        count[i]+=1

    for i in count:
        if count[i]>1:
            res.append(i)

    return res

#driver code

print(duplicate("aabbccdddefgggg"))

        
