#Height of tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return -1
    left_height = height(node.left)
    right_height = height(node.right)
    total_height = max(left_height,right_height)+1
    return total_height

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(height(root))
