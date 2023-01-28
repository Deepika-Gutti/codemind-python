n=int(input())
a=list(map(int,input().split()))
o=0
for i in range(0,n):
    if(a[i]%2!=0):
        o=o+a[i]
print(o)
        