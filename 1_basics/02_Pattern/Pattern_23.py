##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5

'''

n = 5
for i in range(2*n-1):
    for j in range(2*n-1):
        if i==0 or i==2*n-2 or j==0 or j==2*n-2:     ##if i==0 or i==8 or j==0 or j==8:   print(5)
            print(n,end=" ")
        elif i==1 or i==2*n-3 or j==1 or j==2*n-3:
            print(n-1,end=" ")
        elif i==2 or i==2*n-4 or j==2 or j==2*n-4:
            print(n-2,end=" ")
        elif i==3 or i==2*n-5 or j==3 or j==2*n-5:
            print(n-3,end=" ")
        elif i==4 or i==2*n-6 or j==4 or j==2*n-6:
            print(n-4,end=" ")
        else:
            print(1,end=" ")
    print()

    

## another method##
n = 5
for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        bottom = 2*n-2-i
        right = 2*n-2-j

        layer = min(top, left, bottom, right)
        print(n-layer, end=" ")
    print()