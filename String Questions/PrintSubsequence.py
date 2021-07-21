#Print all subsequence of a string

def subseq(s,res):
    if len(s) == 0:
        print(res)
        return
    subseq(s[1:],res+s[0])
    subseq(s[1:],res)


#driver code

subseq("abcd","")