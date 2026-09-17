##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

'''

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    ch = 65
    for j in range(2*i+1):
        print((chr(ch)),end="")
        if j<i:
            ch = ch+1 ##increase character=a,b,c
        else:
            ch = ch-1 ##decrease character=c,b,a
    print()