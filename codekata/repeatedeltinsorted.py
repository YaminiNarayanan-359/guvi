j=int(input())
n=list(map(int,input().split()))
l=[]
for x in range(k):
    for i in range(x+1,len(n)):
        if(n[i]==n[x]):
          l.append(n[x])

if (len(l)==0):
    print("unique")
else:
    l.sort()
    l1=set(l)
    for x in l1:
        print(x,end=" ")
