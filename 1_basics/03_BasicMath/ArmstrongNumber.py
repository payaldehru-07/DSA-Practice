##You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

n = int(input("Enter a number: "))
original = n
temp = n
count = 0
total = 0
while temp > 0:             # Count the number of digits
    count += 1
    temp = temp // 10
while n > 0:            # Calculate Armstrong sum
    digit = n % 10
    total = total + (digit ** count)
    n = n // 10
if total == original:
    print("True")
else:
    print("False") 

##Time Complexity = O(logn)        space Complexity = O(1)