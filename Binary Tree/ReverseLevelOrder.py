#Reverse Level Order Traversal of a Binary Tree
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def reverselevelordertraversal(root):
    queue = []
    stack = []
    queue.append(root)
    while(queue):
        node = queue.pop(0)
        stack.append(node.data)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    print(stack[::-1])

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

reverselevelordertraversal(root)
