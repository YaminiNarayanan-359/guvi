f,g=map(int,input().split())
l=[]
for i in range(1,g+1):
  if(f%i==0 and g%i==0):
    l.append(i)
print(max(l))
