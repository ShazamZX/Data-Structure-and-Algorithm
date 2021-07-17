#cyclic rotation by 1
def rotate(arr):
    return list(arr[-1:]+arr[:len(arr)-1])

#driver code

arr = list(map(int,input().split()))
print(*rotate(arr))