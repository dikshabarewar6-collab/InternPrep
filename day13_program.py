#1. List from normal loop

numbers = []

for i in range(1, 11):
    numbers.append(i)

print(numbers)


#2. List comprehension (same kaam ek line me)

numbers = [i for i in range(1, 11)]

print(numbers)


#3.Square number

squares = []

for i in range(1,6):
    squares.append(i*i)

print(squares)


#4. Condition
evens = []

for i in range(1,11):
    if i % 2 == 0:
        evens.append(i)

print(evens)

#5. String

name = "Diksha"

letters = [ch for ch in name]

print(letters)


#6.Filtering Data

numbers = [20, 55, 70, 10, 90]

result = [n for n in numbers if n > 50]

print(result)


#7. mini project- Vowel extractor

text = "Artificial Intelligence"

vowels = [ch for ch in text if ch.lower() in "aeiou"]

print(vowels)