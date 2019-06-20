p,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(0,p):
  if(l[i]==k):
    print("Yes")
    break
else:
  print("No")
