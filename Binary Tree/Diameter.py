#Diameter of BT - Dist between 2 farthest nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#This will together store the height and diameter assuming each node as root
class Pair:
    def __init__(self):
        self.diameter = 0
        self.height = 0

def diameter(node):
    if node is None:
        answer_pair = Pair()
        answer_pair.height = 0
        answer_pair.diameter = 0
        return answer_pair
    left_pair = diameter(node.left)
    right_pair = diameter(node.right)

    answer_pair = Pair()
    answer_pair.height = max(left_pair.height, right_pair.height) + 1
    #diameter will be max in either left subtree or right subtree or it will pass through root in which case it'll be the sum of the deepest node in l-subt and r-subt + 2 vertices joining them
    answer_pair.diameter = max((left_pair.height + right_pair.height+1),max(left_pair.diameter,right_pair.diameter))

    return answer_pair

#driver code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(diameter(root).diameter)


