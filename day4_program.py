#Nested Loop

for i in range(3):
    for j in range(2):
        print(i, j)


#Pattern Printing
#Pattern1:Square Pattern

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

#Pattern2:Right Triangle
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

#Pattern3:Reverse Triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#Break Statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#Continue Statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
