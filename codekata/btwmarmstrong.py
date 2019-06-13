s,m=input().split()
s=int(s)
m=int(m)
for k in range(s+1,m):
  d=k
  r=0
  while(d>0):
    t=d%10
    d=d//10
    c=t**3
    r=r+c
    if(k==r):
      print(k,end=' ')
