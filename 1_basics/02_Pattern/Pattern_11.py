##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
'''

n = 5
for i in range(n):
    for j in range(i+1):
        print(1 - ((i + j) % 2),end=" ")
    print()
