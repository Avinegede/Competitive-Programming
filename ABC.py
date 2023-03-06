def spl(text):
    return [char for char in text]
a=[int(i) for i in input().split()]
a.sort()
l = spl(input())
d = {
    'A': a[0],
    'B': a[1],
    'C': a[2]
    }
s=""
for el in l:
    print(d[el], end=" ")