"""

Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 


1.Each student gets one packet.
2. The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

"""
import sys
def chocolate(arr,m):
    arr.sort()
    res = sys.maxsize
    i = 0
    while((i+m-1) < len(arr)):
        res = min(res,(arr[i+m-1]-arr[i]))
        i+=1
    return res

print(chocolate([7, 3, 2, 4, 9, 12, 56],3))

    

