#find the row with maximum no of ones in row sorted 0-1 array

def max_ones(mat,R,C):
    count = 0
    j = C-1
    for i in range(R):
        while(j>=0 and mat[i][j] ==1):
            j-=1 #eventually brings to the first occurance of 1 in a column
            count = i #sets it to that corresponding row
    if (count == 0 and mat[i][C-1] ==0):
        return -1
    return count


    #driver code

mat = [[0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
    max_ones(mat,4,4))
