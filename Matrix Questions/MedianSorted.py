#Find median of a sorted matrix
from bisect import bisect_right as upperbound
def median(mat,R,C):
    high = mat[0][C-1]
    low = mat[0][0]
    for i in range(R):
        high = max(high,mat[i][C-1])
        low = min(low,mat[i][0])
    median_calc = (R*C+1)//2
    while(low < high):
        mid = low + (high-low)//2
        count = 0 #count of elements less than mid
        for i in range(R):
            count += upperbound(mat[i],mid)
        if count<median_calc:
            low = mid+1
        else:
            high = mid
    return low

#driver code

r, d = 3, 3
 
m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
print(median(m, r, d))