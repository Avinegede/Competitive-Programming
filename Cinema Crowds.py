a,b = map(int, input().split())
c = [int(i) for i in input().split()]
d = 0
cnt = 0
for i in range( b ) :
    d+= c[i]
    cnt += 1
    if d > a :
        d -= c[i]
        cnt -= 1
print( b-cnt )