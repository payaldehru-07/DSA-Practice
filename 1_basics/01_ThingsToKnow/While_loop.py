##Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.
## A number ends with digit 2 if its last digit is 2.

d = int(input("Enter digit: "))
if d == 0:
    num = 10
else:
    num = d
sum = 0
i = 0
while i < 50:
    sum = sum + num
    num = num + 10
    i = i + 1
print("Sum =", sum)