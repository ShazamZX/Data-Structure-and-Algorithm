#Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b) over all choices of indexes such that both c > a and d > b.
import sys

def func(mat):
    res = -sys.maxsize -1
    N = len(mat)
    dp = [[None for _ in range(N)] for _ in range(N)]
    dp[N-1][N-1] = mat[N-1][N-1]
    
    #filling last row
    for i in range(N-2,-1,-1):
        dp[N-1][i] = max(dp[N-1][i+1],mat[N-1][i])
         
    #filling last column    
    
    for i in range(N-2,-1,-1):
        dp[i][N-1] = max(dp[i+1][N-1],mat[i][N-1])
         

    # filling rest of the column

    for i in range(N-2,-1,-1):
        for j in range(N-2,-1,-1):
            #check whether current spot is the first index of the pair
            res = max(res,(dp[i+1][j+1]-mat[i][j]))
            dp[i][j] = max(mat[i][j],max(dp[i+1][j],dp[i][j+1]))
    return res


#driver code

mat = [[ 1, 2, -1, -4, -20 ],
       [ -8, -3, 4, 2, 1 ],
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6 ],
       [ 0, -4, 10, -5, 1 ]]

print(func(mat))
    


