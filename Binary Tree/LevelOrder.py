#Level Order Traversal of a Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def levelordertraversal(root):
    queue = []
    queue.append(root)
    while(queue):
        size = len(queue)
        for i in range(size):
            curr_node = queue.pop(0)
            print(curr_node.data, end=" ")
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

levelordertraversal(root)
