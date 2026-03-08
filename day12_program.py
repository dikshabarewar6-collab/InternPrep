#1.Import Module

import math

print(math.sqrt(16))

#2.Import special function

from math import sqrt

print(sqrt(25))


#3. Random module (different no. in every run)

import random

num = random.randint(1, 10)

print(num)


#4.Datetime module

import datetime

now = datetime.datetime.now()

print(now)


#5. Project: Random Password Generator

import random

characters = "abcdefghijklmnopqrstuvwxyz123456789"

password = " "

for i in range(6):
    password += random.choice(characters)

print("Generated Password:", password)