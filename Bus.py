x=int(input())
for i in range(x):
    y=int(input())
    ls=[]
    for i in range(y):
        ls.append(2**i)
    print(sum(ls))