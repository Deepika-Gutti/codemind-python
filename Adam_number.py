n=int(input())
import math
a=str(n)[::-1]
a_c=int(a)
a_sc=a_c*a_c
b=str(a_sc)[::-1]
c=n*n
if c==int(b):
    print("True")
else:
    print("False")