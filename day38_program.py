#Delete Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

# delete 20
current = n1

while current.next:
    if current.next.data == 20:
        current.next = current.next.next
        break
    current = current.next

#Reverse Linked List

current = n1
prev = None

while current:
    next_node = current.next   # store next
    current.next = prev        # reverse link
    prev = current             # move prev
    current = next_node        # move current

# new head
n1 = prev


#Print after reverse

current = n1

while current:
    print(current.data)
    current = current.next


#count nodes

count = 0
current = n1

while current:
    count += 1
    current = current.next

print("Count:", count)