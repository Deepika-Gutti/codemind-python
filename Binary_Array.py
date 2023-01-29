n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(i>=2):
        print("False")
        break
else:
    print("True")