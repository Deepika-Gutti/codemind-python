n=int(input())
s=0
res = list(map(int, str(n)))
for i in range(len(res)):
    s+=res[i]**(i+1)
if s==n:
    print("True")
else:
    print("False")
