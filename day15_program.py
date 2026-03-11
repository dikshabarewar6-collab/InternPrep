#1. Class + Object

class Student:
    name = "Diksha"
    course = "AIML"

s1 = Student()

print(s1.name)
print(s1.course)


#2. Constructor + Object

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

s1 = Student("Diksha", "AIML")

print(s1.name)
print(s1.course)


#3. Method in class

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s1 = Student("Diksha")
s1.greet()

#4.Mini Project: Robot class

class Robot:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "says Hello!")

r1 = Robot("AI Robot")

r1.speak()
