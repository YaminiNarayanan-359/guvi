f=int(input())
g,h=map(int,input().split())
for i in range(g+1,h):
  if(i==f):
    print('yes')
    break
else:
  print('no')
