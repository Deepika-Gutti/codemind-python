from math import sqrt
def isprime(n):
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if n>=2:
    t2=n
    t1=n
    t1=t1+1
    while True:
        if isprime(t1):
            break
        else:
            t1=t1+1
    t2=t2-1
    while True:
         if isprime(t2):
             break
         else:
             t2=t2-1
    if isprime(n):
        d=0
        print(d)
    else:
        print(min(abs(t1-n),abs(t2-n)))
    