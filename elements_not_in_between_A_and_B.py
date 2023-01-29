n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
for i in a:
    if(i<c or i>d):
        s=1
        print(i,end=" ")
if(s==0):
    print(-1)
        