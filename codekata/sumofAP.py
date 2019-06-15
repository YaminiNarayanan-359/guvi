j,k,l=list(map(int,input().split()))
c=0
for i in range(1,l+1):
  c+=j+(i-1)*k
print(c)
