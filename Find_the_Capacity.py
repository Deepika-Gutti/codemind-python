a,b,c=list(map(int,input().split()))
cap=2*a*b*c*512
ans=cap//1024
print(ans,end="KB")
