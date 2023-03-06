x=int(input())
dic={}
for i in range(x):
    dic[i]=2**i
for i in dic:
    if(x<=dic[i]):
        print(i+1)
        break