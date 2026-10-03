##You are given an integer n. Return the value of n! or n factorial.

def factorial(n):
    if n == 0:
        return 1
    ans= n*factorial(n-1)
    return ans
n = int(input("enter a number:"))
print(factorial(n))

