#Sort a matrix without using extra space

def sort(mat,R,C):
    size = R * C
    for i in range(size):
        for j in range(size-1):
            if mat[j//C][j%C] > mat[(j+1)//C][(j+1)%C]:
                 mat[j//C][j%C], mat[(j+1)//C][(j+1)%C] = mat[(j+1)//C][(j+1)%C], mat[j//C][j%C]
    


#driver code

mat = [ [5, 4, 7],
            [1, 3, 8],
            [2, 9, 6] ]
row = len(mat)
col = len(mat[0])
sort(mat, row, col)
print(*mat)

