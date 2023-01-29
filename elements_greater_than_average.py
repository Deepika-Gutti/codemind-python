n=int(input())
a=list(map(int,input().split()))
c=0
s=sum(a)
avg=s//n
for i in a:
    if(i>=avg):
        c=c+1
print(c)