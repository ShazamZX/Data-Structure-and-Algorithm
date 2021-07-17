TOP = -1

#calculates area of the largest rectangle in a histogram of an array
def largestHist(arr):
    #right bound
    n = len(arr)
    stack = [] #to store index of elements on right 
    rb = [None]*n #rightbound at position arr[i] stores index of rightmost lower element
    rb[n-1] = n #assume the end and beginning of the array is a ditch and last index of that ditch is array length
    stack.append(n-1)
    for i in range(n-2,-1,-1):
        while(stack and arr[stack[TOP]] > arr[i] ):  
            stack.pop() #only pops element which are greater than current element
        if not stack:
            rb[i] = n
        else:
            rb[i] = stack[TOP]
        stack.append(i)

    stack = [] #to store index of elements on right 
    lb = [None]*n #leftbound at position arr[i] stores index of leftmost lower element
    lb[0] = -1 #assume the end and beginning of the array is a ditch and last index of that ditch is array length
    stack.append(-1)
    for i in range(1,n):
        while(stack and arr[stack[TOP]] > arr[i] ):
            stack.pop()
        if not stack:
            lb[i] = -1
        else:
            lb[i] = stack[TOP]
        stack.append(i)
    
    area = -1

    for i in range(n):
        area = max(area,((rb[i]-lb[i]-1)*arr[i]))
    return area

def largestRectangle(mat):
    R = len(mat)
    C = len(mat[0])
    dp = mat[0] #histogram for each row
    res = largestHist(dp)
    for r in range(1,R):
        for c in range(C):
            if mat[r][c] == 0:
                dp[c] = 0
            else:
                dp[c]+= mat[r][c]
        res = max(res,largestHist(dp))
    return res




#driver code
A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
print(largestRectangle(A))
