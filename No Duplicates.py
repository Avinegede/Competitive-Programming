word = input().strip().split()
l=[]
for i in word:
    if not i in l:
        l.append(i)

if len(word)==len(l):
    print("yes")
else:
    print("no")