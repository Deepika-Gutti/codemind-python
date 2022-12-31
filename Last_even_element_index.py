n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr[::-1]:
    c=c+1
    if(i%2==0):
        break
print(n-c)
