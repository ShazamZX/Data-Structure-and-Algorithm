#Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details. 



def wordbreak(dictionary,sentence):
    sentence = "$"+sentence #$ stands for null string
    n = len(sentence)
    dp = [False]*(n)

    dp[0] = True #Assume that making null string is always possible

    for i in range(1,n):
        for j in range(1,i+1):
            if sentence[j:i+1] in dictionary and dp[j-1] is True:
                dp[i] = True
    # print(*dp)
    return dp[n-1]


#Driver Code

dictionary = set(["mobile","samsung","sam","sung","man","mango",
                           "icecream","and","go","i","like","ice","cream"])

print(wordbreak(dictionary,"ilikeicecreamandmango"))


