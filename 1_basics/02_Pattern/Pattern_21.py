##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

'''

n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for j in range(2*(n-i-1)):
        print(" ",end="")
    for i in range(i+1):
        print("*",end="")
    print()
n = 5
for i in range(1,n): ## we have to print middle line once so we set limit
    for j in range(n-i):
        print("*",end="")
    for j in range(2*i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    print()