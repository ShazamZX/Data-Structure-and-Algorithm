#Rotate a matrix by 90 degree to the right


#first transpose the matrix(-90deg) and then reverse it row-wise(180deg)
def rotate(mat):
    N = len(mat)
    #transpose
    for i in range(N):
        for j in range(i,N):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    #reverse
    for i in range(N):
        left = 0
        right = N-1
        while(left<right):
            mat[i][left], mat[i][right] = mat[i][right], mat[i][left]
            left+=1
            right-=1


#driver code
arr = [ [ 1, 2, 3, 4 ],
          [ 5, 6, 7, 8 ],
          [ 9, 10, 11, 12 ],
          [ 13, 14, 15, 16 ] ]  
rotate(arr)
print(arr)