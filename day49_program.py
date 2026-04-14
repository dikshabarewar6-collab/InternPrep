# Star pattern
n = 4

for i in range(1, n+1):
    print("*" * i)

# Reverse Pattern
n = 4

for i in range(n, 0, -1):
    print("*" * i)

# Number Pattern
n = 4

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


