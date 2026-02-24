
#Hello world program
print("Hello World")


#Name input + Greeting
name = input("Enter your name: ")
print("Hello", name, "Welcome!")



#Even Odd Check
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#Positive/Negative/Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#Addition of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
print("Sum is:", sum)


#If else condition
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")