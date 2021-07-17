#Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it. Note: In a path, no cell can be visited more than one time.
def dfs(mat,path,i,j,res,visited,n):
    if i<0 or j<0 or i>=n or j>=n or mat[i][j] == 0 or visited[i][j] == True:
        return
    if i == n-1 and j==n-1:
        res.append(path)
        return

    visited[i][j] = True
    
    dfs(mat,path+"U",i-1,j,res,visited,n)
    dfs(mat,path+"D",i+1,j,res,visited,n)
    dfs(mat,path+"L",i,j-1,res,visited,n)
    dfs(mat,path+"R",i,j+1,res,visited,n)

    visited[i][j] = False 
    


def search(mat):
    n = len(mat)
    if mat[0][0] == 0 or mat[n-1][n-1] == 0:
        return [-1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    res = []
    dfs(mat,"",0,0,res,visited,n)
    return sorted(res)


#driver code

m = [ [ 1, 0, 0, 0, 0 ], 
          [ 1, 1, 1, 1, 1 ], 
          [ 1, 1, 1, 0, 1 ], 
          [ 0, 0, 0, 0, 1 ],
          [ 0, 0, 0, 0, 1 ] ]
print(search(m))


    

    
