N=int(input())
li=[]
for i in range(0,N):
    li.append(list(map(int,input().split())))
p=0
k=0
for i in range(0,N):
    for j in range(0,N):
        if li[i][j]==1:
            if i!=N-1 and li[i+1][j]==0:
                p=p+1
            if j!=N-1 and li[i][j+1]==0:
                p=p+1
            if i!=0 and li[i-1][j]==0:
                p=p+1
            if j!=0 and li[i][j-1]==0:
                p=p+1
            if i==0 and j==0 or i==N-1 and j==N-1  or i==0 and j==N-1 or i==N-1 and j==0 and c==2:
                k=k+1
            elif i==1 and j>0 and j<N-1 and c==3:
                k=k+1
            elif c==4:
                k=k+1
        c=0
                
print(k)
