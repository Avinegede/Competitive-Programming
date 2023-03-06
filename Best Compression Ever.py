a,b=map(int,input().split())
s=0
for i in range(0,(b+1)):
    s=s+2**i
if (s>=a):
    print("yes")
else:
    print("no")