s,d=map(int,input().split())
g=[int(i) for i in input().split()]
h=0
for j in g:
  if(j==d):
    h=h+1
print(h)
