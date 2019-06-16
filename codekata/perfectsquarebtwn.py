k,l=map(int,input().split())
l1=[]
c=0
for i in range(1,l+1):
    sq=i*i
    if(sq<=l):
        l1.append(i*i)
    else:
        break
for j in range(k,l+1):
    if(j in l1):
        c+=1
print(c)
