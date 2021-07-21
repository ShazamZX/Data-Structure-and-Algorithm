#Given a string, find the length of the longest repeating subsequence such that the two subsequences don't have same string character at the same position, i.e., any i'th character in the two subsequences shouldn't have the same index in the original string. 



def LPS(s):
    n = len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == s[j-1] and i!=j: #LCS logic however the characters must not have the same index
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    LCS = ""
    #backtracking dp matrix to find LCS

    i,j = n,n
    while(i>0 and j>0):    
        if s[i-1] == s[j-1] and i!=j:
            LCS+=s[i-1]
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
    return LCS[::-1]

#driver code

print(LPS("aab"))