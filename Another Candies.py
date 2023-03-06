x=int(input())
for i in range(x):
    p=input()
    y=int(input())
    lsy=[]
    for i in range(y):
        m=int(input())
        lsy.append(m)
    if(sum(lsy)%y==0):
        print("Yes")
    else:
        print("No")