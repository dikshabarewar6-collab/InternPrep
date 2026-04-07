# Binary Search Tree
# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# insert in BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

# Create BST
root = None

root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 20)
root = insert(root, 2)
root = insert(root, 8)

# Search in BST
def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
    

# Check Search
result = search(root, 8)

if result:
    print("Found")
else:
    print("Not Found")