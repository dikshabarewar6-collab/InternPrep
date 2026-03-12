#1. Parent Class
class Animal:
    def speak(self):
        print("Animal makes sound")

#2. Child Class
class Dog(Animal):
    def bark(self):
        print("Dog Barks")

#3.Object Create
d = Dog()

d.speak()
d.bark()

#4. Constructor Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def show(self):
        print("Name:", self.name)

s = Student("Diksha")
s.show()


#5. Method Overriding
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()

#6. Mini Project: Robot System
class Robot:
    def move(self):
        print("Robot moving")

class CleaningRobot(Robot):
    def clean(self):
        print("Cleaning floor")

r = CleaningRobot()
r.move()
r.clean()