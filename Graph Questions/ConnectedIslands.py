#Find connected components in an adj matrix

  

def dfs(mat,i,j,visited,n):
    if i<0 or j<0 or i>=n or j>=n or mat[i][j] ==0 or visited[i][j]:
        return
    visited[i][j] = True
    dfs(mat,i-1,j,visited,n)
    dfs(mat,i+1,j,visited,n)
    dfs(mat,i,j-1,visited,n)
    dfs(mat,i,j+1,visited,n)
    dfs(mat,i-1,j-1,visited,n)
    dfs(mat,i-1,j+1,visited,n)
    dfs(mat,i+1,j-1,visited,n)
    dfs(mat,i+1,j+1,visited,n)

def findComponents(mat):
    n = len(mat)
    components = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1 and not visited[i][j]:
                dfs(mat,i,j,visited,n)
                components+=1
    return components

#driver code

graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

print(findComponents(graph))





