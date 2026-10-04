##Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.

def num(n):
    if n == 0:
        return
    print(n)
    num(n - 1)
n = int(input("enter a number:"))
num(n)


