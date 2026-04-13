#Maximun slement
arr = [4, 9, 2, 7]

max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print("Max:", max_val)


#Reverse array
arr = [1,2,3,4]

rev = []

for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])

print(rev)


#Palindrome check
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")