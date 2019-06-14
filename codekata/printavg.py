o=int(input())
a=[int(j) for j in input().split()]
sum=0
for i in a:
  sum=sum+i
  m=sum//o
print(m)
