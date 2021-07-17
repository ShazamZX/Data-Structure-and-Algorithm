#find the longest palindrom substring in a given string(O(N^2) solution)


def longestpalin(s):
    start = 0
    n = len(s)
    maxlen = 0
    #for odd combination of palindrome
    for i in range(1,n):
        left = i-1
        right = i+1
        while(left >= 0 and right < n and s[left] == s[right]):
            if right-left+1 >maxlen:
                start = left
                maxlen = right-left+1
            left-=1
            right+=1
    
    #for even length palins
    for i in range(1,n):
        left = i-1
        right = i
        while(left >= 0 and right < n and s[left] == s[right]):
            if right-left+1 >maxlen:
                start = left
                maxlen = right-left+1
            left-=1
            right+=1
    
    return s[start:(start+maxlen)]


#driver code


print(longestpalin("heymadamiambobbob"))

