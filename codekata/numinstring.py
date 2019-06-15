k=input()
l=[]
for i in k:
  if(i.isnumeric()):
    l.append(i)
print(*l,sep='')
