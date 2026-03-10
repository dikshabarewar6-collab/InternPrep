#1. Lambda Function

add = lambda a, b: a + b

print(add(5, 3))


#2. Square
square = lambda x: x * x

print(square(6))


#3.Lambda with Map
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x*x, numbers))

print(squares)

#4. Lambda with filter
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

#5. Lambda with sorted
students = [("Diksha", 97), ("Riya", 85), ("Aman", 70)] 

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)


#6. Mini Project-Price Discount
prices = [100, 200, 300]

discount_prices = list(map(lambda p: p*0.9, prices))

print(discount_prices)