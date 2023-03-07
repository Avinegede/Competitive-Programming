line =input()
a,b =line.split()
a = int(a)
b = int(b)
l =[]
l.append(a)
l.append(b)
p=sorted(l)
s=""
for i in range(2):
    s=str(s)+" "+str(p[i])
print(s)