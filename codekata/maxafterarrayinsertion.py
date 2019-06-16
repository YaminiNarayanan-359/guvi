i,j=map(int,input().split()) 
e=input()
m=list(map(int,input().split()))
h=list(map(int,input().split()))
p=[]
for v in range(j):
    m.append(h[v])
    p.append(max(m))
print(*p)
