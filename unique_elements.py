n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i not in l:
        l.append(i)
for i in l:
    print(i,end=" ")