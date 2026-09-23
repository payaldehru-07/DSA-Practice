##You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.

n = int(input("enter a number:"))
divisor = []
for i in range(1,n+1):
    if n % i == 0:
        divisor.append(i)
print(divisor)

##Time Complexity = O(n)        space Complexity = O(1)