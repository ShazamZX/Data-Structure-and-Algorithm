#Search in a sorted matrix

def search(mat,R,C,element):
    i = 0
    j = C-1
    while(i<R and j>=0):
        if mat[i][j] == element:
            print(f"Element found at ({i},{j})")
            return 
        if mat[i][j] < element:
            i+=1
        else:
            j-=1
    print("Element Not Found")
    return 


#driver code

mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48]]
search(mat, 3, 4, 35)