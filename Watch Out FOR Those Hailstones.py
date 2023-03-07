r=int(input())
ls=[r]
x=r
while x!=1:
    if(x%2==0):
        y=int(x/2)
        ls.append(y)
        x=y
    else:
        y=int((3*x)+1)
        ls.append(y)
        x=y       
print(sum(ls))