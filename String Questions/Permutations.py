#Print all permutations of a string(Approach: Backtracking)

def permute(s):
    def permute_util(s,l,r):
        if l==r:
            print("".join(s))
            return

        for i in range(l,r+1):
            s[i],s[l] = s[l],s[i]
            permute_util(s,l+1,r)
            s[i],s[l] = s[l],s[i]
    permute_util(s,0,len(s)-1)

#driver code

permute(list("ABCD"))