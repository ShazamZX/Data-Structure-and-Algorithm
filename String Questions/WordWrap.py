"""
Given a sequence of words, and a limit on the number of characters that can be put in one line (line width). Put line breaks in the given sequence such that the lines are printed neatly. Assume that the length of each word is smaller than the line width. When line breaks are inserted there is a possibility that extra spaces are present in each line. The extra spaces includes spaces put at the end of every line except the last one. 
The problem is to minimize the following total cost. 
Total cost = Sum of cost of all lines, where cost of line is = (Number of extra spaces in the line)^2. 
"""

import sys

def wordwrap(arr,k):
    n = len(arr)
    dp = [sys.maxsize]*n  #this stores the cost if the ith word is the starting word
    end_word = [0]*n #store the ending word if ith word is the first word
    cost:int

    dp[n-1] = 0 #if the last word is the starting word then the cost would be 0 since the extra spaces in last line is not counted
    end_word[n-1] = n-1 #if last word is first word then its also the last word in the line

    for i in range(n-2,-1,-1):
        cur_len = -1 #because the first word to be processed wont have a leading separation space
      

        for j in range(i,n):
            cur_len+=(arr[j]+1) #+1 for adding a word separation space before the word

            if cur_len>k:
                break

            if j==n-1:
                cost = 0 #if j reaches the last word that means its the last line so cost would be zero
            else:
                #cost would be cost of current length as well as cost of the words which are in the next line
                cost = (k-cur_len)*(k-cur_len) + dp[j+1]

            if cost<dp[i]:
                dp[i] = cost
                end_word[i] = j

        #printing the words with line

    i = 0
    while(i<n):
        print((i+1),(end_word[i]+1)) #Starting word , end_word of that line
        i=end_word[i]+1 #points to the next word from prev iteration end word


#driver code

arr = [3, 2, 2, 5 ]
k = 6

wordwrap(arr,k)