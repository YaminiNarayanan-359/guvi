e,r=map(int,input().split())
h=e*r
for i in range(0,h+1):
  if(i**2==h):
    print('yes')
    break
else:
  print('no')
