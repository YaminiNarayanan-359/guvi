i=int(input())
j=list(map(int,input().split()))
k=j[:]
k.sort()
for v in range(0,len(j)):
  if(j[v]!=k[v]):
    print(v)
    break
