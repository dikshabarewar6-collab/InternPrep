import random

# random number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess (1-100): "))

    if guess == number:
        print("🎉 Correct! You guessed it!")
        break

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Too low! Try again.")