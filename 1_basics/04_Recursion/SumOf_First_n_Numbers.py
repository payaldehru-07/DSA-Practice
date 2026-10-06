##Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

def num(n):
    if n == 0:
        return 0
    ans = num(n - 1) + n
    return ans
n = int(input("Enter a number: "))
print(num(n))


