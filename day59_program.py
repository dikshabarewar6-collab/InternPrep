#Find first duplicate
arr = [1, 3, 4, 2, 2]

seen = set()

for num in arr:
    if num in seen:
        print("Duplicate:", num)
        break
    seen.add(num)



#valid parentheses
text = "()[]{}"

stack = []
pairs = {')':'(', ']':'[', '}':'{'}

for ch in text:
    if ch in pairs.values():
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            print(False)
            break
        stack.pop()
else:
    print(True)




# longest substring without repeat
text = "abcabcbb"

seen = set()
left = 0
max_len = 0

for right in range(len(text)):
    while text[right] in seen:
        seen.remove(text[left])
        left += 1

    seen.add(text[right])
    max_len = max(max_len, right - left + 1)

print(max_len)