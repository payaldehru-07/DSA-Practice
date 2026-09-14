##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
12345
1234
123
12
1


i           r           j           o
0           5           0,1,2,3,4   12345
1           4           0,1,2,3     1234
2           3           0,1,2       123
3           2           0,1         12
4           1           0           1


n = 5
for i in range(n):
    for j in range(n-i):
        print(j+1,end ="")
    print()
'''


n = 4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range((i*2)+1):
        print("*",end="")
    print()
