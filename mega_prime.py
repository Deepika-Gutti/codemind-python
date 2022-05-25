def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
n=int(input())
prime(n)
if prime(n):
    b=list(map(int,str(n)))
    k=0
    for j in range(0,len(b)):
        prime(b[j])
        if prime(b[j]):
            k=k+1
        else:
            print("Not Mega Prime")
            break
    if k==len(b):
        print("Mega Prime")
else:
    print("Not Mega Prime")