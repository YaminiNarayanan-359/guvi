p,o=input().split()
p=int(p)
o=int(o)
n=0
arr=[int(i) for i in input().split()]
for s in range(0,o):
  n=n+arr[s]
print(n)
