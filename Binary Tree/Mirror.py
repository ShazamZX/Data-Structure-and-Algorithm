#print inorder of mirror image of a B-Tree

class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def invert(node):
    if node is None:
        return
    left = invert(node.left)
    right = invert(node.right)

    node.left = right
    node.right = left
    return node


#driver code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Original Tree')
inorder(root)
print('\nInverted Tree')

inorder(invert(root))