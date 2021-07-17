#Merge intervals - scheduling 

def mergeInterval(intervals):
    intervals.sort(key= lambda x:x[0])
    end = -1
    start = -1
    res = []
    for i in range(len(intervals)):
        a = intervals[i]
        if a[0] > end:
            if i!= 0:
                res.append([start, end])
            start = a[0]
            end = a[1]
        else:
            if a[1]>=end:
                end = a[1]
    
    if end!= -1 and [start,end] not in res:
        res.append([start, end])
    print(*res)


#driver code

arr=  [[2,4], [1,3],[6,8],[5,7]]
mergeInterval(arr)
            

