g,k=input().split()
g=int(g)
k=int(k)
for t in range(g+1,k):
  if(t>1):
    for j in range(2,t):
      if(t%j==0):
        break
    else:
      print(t,end=' ')
  else:
    break
