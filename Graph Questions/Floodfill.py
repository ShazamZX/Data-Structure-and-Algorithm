#Replace a colored patch by another
def check(x,y,n,prev_color,new_color,screen):
    if x>=0 and y>=0 and x<n and y<n and screen[x][y] == prev_color:
        return True
    return False

def floodfill(screen, index,color):
    n = len(screen)
    queue = []
    queue.append(index)
    prev_color = screen[index[0]][index[1]]
    screen[index[0]][index[1]] = color

    while queue:
        curr_index = queue.pop(0)
        x = curr_index[0]
        y = curr_index[1]

        if check(x-1,y,n,prev_color,color,screen):
            queue.append((x-1,y))
            screen[x-1][y] = color

        if check(x+1,y,n,prev_color,color,screen):
            queue.append((x+1,y))
            screen[x+1][y] = color

        if check(x,y-1,n,prev_color,color,screen):
            queue.append((x,y-1))
            screen[x][y-1] = color
            
        if check(x,y+1,n,prev_color,color,screen):
            queue.append((x,y+1))
            screen[x][y+1] = color


#driver code

screen =[
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0],
[1, 0, 0, 1, 1, 0, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[1, 1, 1, 1, 1, 2, 2, 1],
    ]
     
# Row of the display
m = len(screen)
 
# Column of the display
n = len(screen[0])
 
# Co-ordinate provided by the user
index = (4,4)
 
# Current color at that co-ordinate

 
# New color that has to be filled
newC = 3
 
floodfill(screen,index, newC)
 
 
# Printing the updated screen
for i in range(m):
    for j in range(n):
        print(screen[i][j], end =' ')
    print()
