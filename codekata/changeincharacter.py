l,d=input().split()
c=0
for i in range(0,len(l)):
  if(l[i]!=d[i]):
    c=c+1
if(c==1):
  print("yes")
else:
  print("no")
