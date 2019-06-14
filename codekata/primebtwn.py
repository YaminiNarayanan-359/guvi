g,k=input().split()
g=int(g)
k=int(k)
c=0
for t in range(g,k):
  if(t>1):
    for j in range(2,t):
      if(t%j==0):
        break
    else:
      c=c+1
  else:
    break
print(c)
