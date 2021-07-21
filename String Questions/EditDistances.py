"""
Given two strings s and t. Find the minimum number of operations that need to be performed on str1 to convert it to str2. The possible operations are:

Insert
Remove
Replace
"""

def edit(s1,s2):
    r = len(s1)
    c = len(s2)
    dp = [[0 for _ in range(c+1)] for _ in range(r+1)]

    for i in range(r+1):
        for j in range(c+1):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

    return dp[r][c]

#driver code

s1 = "sunday"
s2 = "saturday"
print(edit(s1,s2))