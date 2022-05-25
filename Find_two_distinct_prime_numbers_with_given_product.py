from math import sqrt
def prime(n):
    sq=int(sqrt(n))
    for j in range(2,sq+1):
        if n%j==0:
            return False
    else:
        return True
n=int(input())
if n>2:
    for i in range(2,n//2):
        if n%i==0:
            x=i
            y=n//i
            if prime(x) and prime(y):
                print(x,y)
                break
    else:
        print(-1)