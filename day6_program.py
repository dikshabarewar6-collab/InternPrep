#String indexing
name = "Diksha"

print(name[0])   # D
print(name[3])   # s


#Negative indexing
print(name[-1])  # a
print(name[-2])  # h


#String Slicing
print(name[0:3])   # Dik
print(name[2:6])   # ksha


#Loop in String
name = "Diksha"

for ch in name:
    print(ch)


#Function in String
text = "python programming"

print(text.upper())      # PYTHON PROGRAMMING
print(text.lower())      # python programming
print(text.capitalize()) # Python programming
print(len(text))         # length
print(text.count("p"))   # count p


#Pelindrome checker
word = input("Enter word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#Vowel Counter
text = input("Enter text: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Total vowels:", count)