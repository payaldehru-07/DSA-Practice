##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
'''

n = 5
for i in range(n):
    for j in range(i+1):
        print((n-i+j),end=" ")
    print()
