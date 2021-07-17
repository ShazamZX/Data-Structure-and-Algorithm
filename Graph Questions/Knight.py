#Given a square chessboard of N x N size, the position of Knight and position of a target is given. We need to find out the minimum steps a Knight will take to reach the target position.

class cell:
    def __init__(self,i,j,dist):
        self.i = i
        self.j = j
        self.dist = dist

def steps(knight_pos,target,n):
    # jump(i,j) denotes possible move of the knight
    jump_i = [2, 2, -2, -2, 1, 1, -1, -1]
    jump_j = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue.append(cell(knight_pos[0],knight_pos[1],0)) # starting position of knight
    visited[knight_pos[0]][knight_pos[1]] = True

    while queue:

        curr = queue.pop(0)
        if curr.i == target[0] and curr.j == target[1]:
            return curr.dist

        for pos in range(8):
            next_move_i = curr.i + jump_i[pos]
            next_move_j = curr.j + jump_j[pos]
            if (next_move_j >= 0 and next_move_i >= 0 and next_move_j<n and next_move_i<n) and visited[next_move_i][next_move_j] == False:
                queue.append(cell(next_move_i,next_move_j,curr.dist+1))
                visited[next_move_i][next_move_j] = True    


#driver code


knightpos = [0, 0]
targetpos = [29, 29]
print(steps(knightpos,targetpos,30))

    

