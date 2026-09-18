##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
E 
D E 
C D E 
B C D E 
A B C D E
'''

n = 5 
for i in range(n):
    for j in range(i+1):
        print(chr(65+(n-1-i)+j),end=" ")
    print()