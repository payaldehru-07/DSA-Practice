##Given marks of a student, print on the screen:Grade A if marks >= 90
##Grade B if marks >= 70 Grade C if marks >= 50 Grade D if marks >= 35 Fail, otherwise.

marks = int(input("enter marks:"))
if (marks>=90):
    print("grade A")
elif marks>=70 and marks<90:
   print("grade B")
elif marks>=50 and marks<70:
    print("grade C")
elif marks>=35 and marks<50:
    print("grade D")
else:
    print("fail")
 