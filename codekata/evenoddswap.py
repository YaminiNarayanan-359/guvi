p=input()
p=list(p)
p[::2],p[1::2]=p[1::2],p[::2]
print(*p,sep='')
