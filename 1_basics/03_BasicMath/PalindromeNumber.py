##You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
## A palindrome number is a number which reads the same both left to right and right to left.

n = int(input("enter a number:"))
rev = 0
original = n
while n > 0:
    digit = n % 10      # Get last digit
    rev = rev*10+digit  # Reverse the number
    n = n//10        
print(rev)
if original == rev:
    print(True)
else:
    print(False)

##Time Complexity: O(log n)   Space Complexity: O(1)##

