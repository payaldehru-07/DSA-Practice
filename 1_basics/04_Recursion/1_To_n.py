##Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion 

def num(n):
    if n == 0:
        return
    num(n - 1)
    print(n)
n = int(input("enter a number:"))
num(n)


