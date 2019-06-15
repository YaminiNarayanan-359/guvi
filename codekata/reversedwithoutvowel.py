p=int(input())
r=input()
r=list(r)
l=[]
for i in r: 
    if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
        l.append(i)
    q=l[::-1]
print(*q,sep="")
