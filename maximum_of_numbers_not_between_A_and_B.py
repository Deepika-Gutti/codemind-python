n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
m=0
mylist=[]
for i in a:
        if(i<b or i>c):
            m=1
            mylist.append(i)
if(m==0):
    print(-1)
print(max(mylist))
