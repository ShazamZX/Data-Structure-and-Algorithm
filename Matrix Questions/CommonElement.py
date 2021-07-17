#find elements common in each row of matrix

def common(mat):
    R= len(mat)
    elements = dict.fromkeys(mat[0],1)
    res = []
    for i in range(1,R):
        for element in mat[i]:
            if element in elements.keys():
                elements[element]+=1
                if elements[element] == R and i==R-1:
                    res.append(element)
    return res

#driver code

mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
 
print(common(mat))
