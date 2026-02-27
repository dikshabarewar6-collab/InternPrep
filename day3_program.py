#For Loop

for i in range(1, 11):
    print(i)


#While Loop

i = 1
while i <= 5:
    print(i)
    i += 1


#Sum of first 10 numbers

total = 0
for i in range(1, 11):
    total += i
print("Sum is:", total)


#Table Generator
num = int(input("Enter numbers: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



#Sensor Monitoring
while True:
    value = int(input("Enter sensor value: "))

    if value >= 100:
        print("Alert!")
        break
    else:
        print("Monitoring...")