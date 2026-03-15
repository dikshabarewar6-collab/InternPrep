#1. Abstract class + Child Class Implementation
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Dog barks")

class Cat(Animal):

    def speak(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.speak()
c.speak()


#2. Mini Project: Payment System
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Card(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")

p1 = UPI()
p2 = Card()

p1.pay(500)
p2.pay(1000)

