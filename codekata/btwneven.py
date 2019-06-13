j,k=input().split()
j=int(j)
k=int(k)
for t in range(j+1,k):
  if(t>0):
    if(t%2==0):
      print(t,end=' ')
