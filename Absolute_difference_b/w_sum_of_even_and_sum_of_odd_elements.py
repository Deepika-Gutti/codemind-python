n=int(input())
a=list(map(int,input().split()))
e=0
o=0
for i in range(0,n):
    if(a[i]%2==0):
        e=e+a[i]
    else:
        o=o+a[i]
print(abs(e-o))