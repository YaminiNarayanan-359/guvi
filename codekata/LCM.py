import math
g,h=input().split()
g=int(g)
h=int(h)
f=(math.gcd(g,h))
print((g*h)//f)
