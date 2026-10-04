##Given a string s, return true if the string is palindrome, otherwise false.

s = input("Enter string: ")
left = 0
right = len(s) - 1
palindrome = True
while left < right:
    if s[left] != s[right]:
        palindrome = False
        break
    left += 1
    right -= 1
if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")


## Time Complexity = O(n)       Space Complexity = O(1)##



