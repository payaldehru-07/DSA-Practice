##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
A
AB
ABC
ABCD
ABCDE
'''

n = 5 
for i in range(n):
    for j in range(i+1):
        print((chr(65+j)),end="")
    print()