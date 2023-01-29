def strickodd(a):
    for i in range(len(a)):
        if(a[i]%2!=0):
            if(i%2==0):
                return False
    return True
n=int(input())
a=list(map(int,input().split()))
print(strickodd(a))
    