
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N =5

'''
*****
*****
*****
*****
*****
'''


n = 5
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()