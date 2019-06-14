s,d=map(int,input().split())
g=list(map(int,input().split()))

for j in g:
  if(j==d):
    print('yes')
    break
else:
  print('no')
