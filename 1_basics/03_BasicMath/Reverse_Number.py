##You are given an integer n. Return the integer formed by placing the digits of n in reverse order.



class Solution:
    def countDigit(self, n):
        revnum = 0
        while n>0:
            ld = n%10
            revnum = (revnum*10)+ld
            n = n//10
        return(revnum)