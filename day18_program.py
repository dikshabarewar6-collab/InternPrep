#1.Method Overriding
class Animal:

    def speak(self):
        print("Animal makes sound")


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


#2.Method Overloading
class Math:

    def add(self, a, b, c=0):
        return a + b + c


m = Math()

print(m.add(2,3))
print(m.add(2,3,4))


#3.Built-in Polymorphism
print(len("Diksha"))
print(len([1,2,3,4]))


#4.Polymorphism with Functions
def show_area(shape):
    shape.area()


class Circle:
    def area(self):
        print("Area of circle")


class Square:
    def area(self):
        print("Area of square")


c = Circle()
s = Square()

show_area(c)
show_area(s)


#5.Mini Project – Shape System
class Shape:

    def draw(self):
        print("Drawing shape")


class Circle(Shape):

    def draw(self):
        print("Drawing circle")


class Rectangle(Shape):

    def draw(self):
        print("Drawing rectangle")


shapes = [Circle(), Rectangle()]

for s in shapes:
    s.draw()