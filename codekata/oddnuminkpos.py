g,h=map(int,input().split())
s=[int(i) for i in input().split()]
l=[]
for j in s:
  if(j%2!=0):
    l.append(j)
print(l[h-1])
