##You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.

n = int(input("enter a number:"))
count = 0
for i in range(1, n+1):
    if(n % i == 0):
        count += 1
    if(count > 2):
        break
if count == 2:
    print("True")
else:
    print("false")

##Time Complexity = O(n)        space Complexity = O(1)
