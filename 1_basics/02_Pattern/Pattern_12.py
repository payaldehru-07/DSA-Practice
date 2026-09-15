##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1        1
12      21
123    321
1234  4321
1234554321

'''

n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    for j in range(2*(n-i-1)):
        print(" ",end="")
    for j in range(i+1):
        print(i+1-j,end="")
    print()