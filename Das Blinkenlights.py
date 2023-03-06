from math import *
c=[int(i) for i in input().split()]
x=int (c[0])
y=int (c[1])
z=int (c[2])
lcm=(x*y)/gcd(x,y)
if (lcm<=z):
    print("yes")
else:
    print("no")