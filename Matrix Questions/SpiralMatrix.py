#Spiral Traversal of a matrix
def spiral(arr,R,C):
    upper = 0
    lower = R-1
    right = C-1
    left = 0
    while(upper<=lower and left<=right):
        for i in range(left,right+1):
            print(arr[upper][i],end=" ")
        upper+=1
        for i in range(upper,lower+1):
            print(arr[i][right],end=" ")
        right-=1
        if(upper<=lower):
            for i in range(right,left-1,-1):
                print(arr[lower][i],end=" ")
            lower-=1
        if(left<=right):
            for i in range(lower,upper-1,-1):
                print(arr[i][left],end=" ")
            left+=1


#driver code

a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
 
R = 3
C = 6
spiral(a,R,C)
print()

b = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
spiral(b,5,5)