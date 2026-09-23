##You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
##The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.##

n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
if n1 < n2:
    limit = n1              #limit = min(n1, n2)
else:
    limit = n2
gcd = 1
for i in range(1,limit+1):
   if n1 % i == 0 and n2 % i == 0:
    gcd = i
print("GCD :", gcd)

##Time Complexity: O(min(n1, n2))     Space Complexity: O(1)##