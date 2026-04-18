# Anagram check
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")



# First non-repeating character
text = "aabbcde"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for ch in text:
    if freq[ch] == 1:
        print("First unique:", ch)
        break



# String compression
text = "aaabbc"

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        result += text[i-1] + str(count)
        count = 1

result += text[-1] + str(count)

print(result)


# check rotation
s1 = "abcd"
s2 = "cdab"

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Rotation")
else:
    print("Not Rotation")



# Longest word in sentence
text = "I love programming"

words = text.split()

longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word:", longest)