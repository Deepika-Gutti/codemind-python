def fib_seq(n):
    a,b=0,1
    if a==n or b==n:
        return True
    c=a+b
    while True:
        if c==n:
            return True
        if c>n:
            return False
        a=b
        b=c
        c=a+b
n=int(input())
print(fib_seq(n))