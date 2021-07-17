#find the max product of all subarrays


def prod(arr):
    max_till_i = arr[0]
    min_till_i = arr[0]
    maxproduct = arr[0]

    for i in range(1,len(arr)):
        #for a negative number the lower value will give a greater product
        if arr[i]<0:
            max_till_i,min_till_i = min_till_i,max_till_i

        max_till_i = max(arr[i],(max_till_i*arr[i]))
        min_till_i = min(arr[i],(min_till_i*arr[i]))

        maxproduct = max(maxproduct,max_till_i)

    return maxproduct

#driver code

print(prod([6, -3, -10, 0, 2]))

print(prod([-6]))