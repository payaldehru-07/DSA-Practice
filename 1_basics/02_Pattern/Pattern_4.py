##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1
22
333
4444
55555
'''

n = 5
for i in range(n):
    for j in range(i+1):
        print(i+1 , end ="")
    print()