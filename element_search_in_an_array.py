n=int(input())
arr=list(map(int,input().split()))
t=int(input())
c=0
for i in range(0,n):
    if(t==arr[i]):
        c+=1
if(c==0):
    print("False")
else:
    print("True")