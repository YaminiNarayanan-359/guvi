j,k,l=input().split()
x=str(j)
y=str(k)
z=int(l)
l=0
for i in range(len(x)):
    if(x[i]!=y[i]):
        l=l+1 
if(z==l):
    print("yes")
else:
    print("no")
