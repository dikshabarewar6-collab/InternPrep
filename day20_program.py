#1. Class & Object

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s1 = Student("Diksha")
s1.greet()



#2.Inheritance

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.speak()
d.bark()



#3.Encapsulation

class Bank:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance
    
b = Bank()

print(b.get_balance())



#4.Polymorphism

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for a in animals:
    a.speak()



#5.Abtraction

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



#6.Mini Project: Library System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Book:", self.title)
        print("Author:", self.author)

b1 = Book("AI Basics", "John Smith")

b1.display()