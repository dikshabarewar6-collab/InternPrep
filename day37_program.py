# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# linking
n1.next = n2
n2.next = n3


# Traversal
current = n1

while current:
    print(current.data)
    current = current.next


# Insertion at beginning
new_node = Node(5)
new_node.next = n1
n1 = new_node


# Insertion at end
new_node = Node(40)

current = n1
while current.next:
    current = current.next

current.next = new_node