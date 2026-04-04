# Stack using list
stack = []

# push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Pop
stack.pop()
print(stack)

# Peek
print(stack[-1])

# Check Empty
if not stack:
    print("Stack is empty")


# Reverse string using stack
text = "Diksha"

stack = []

# push
for ch in text:
    stack.append(ch)

# pop
rev = ""

while stack:
    rev += stack.pop()

print("Reversed:", rev)