# Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Tree
root = Node(10)

root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)


# Traversal

# Inorder(LNR)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

# Preorder(NLR)
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

# Postorder(LRN)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


print("Inorder:")
inorder(root)

print("Preorder:")
preorder(root)

print("Postorder:")
postorder(root)

