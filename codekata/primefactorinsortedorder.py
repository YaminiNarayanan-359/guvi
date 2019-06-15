n=int(input())
for y in range(2,n+1):
    if(n%y==0):
        c=0
        for k in range(1,y+1):
            if(y%k==0):
                c=c+1
        if(c==2):
            print(k,end=" ")
