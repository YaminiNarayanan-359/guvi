l=[]
m=int(input())
a=input().split()
for i in a:
  l.append(i)
l.sort()
l.sort(key=len)
for i in l:
  print (i,end=' ')
