a=input()
a=a.split()
a=list(map(int,a))
b1=int(a[0])
c1=int(a[1])
for i in range(1,b1*c1+1):
    if(i%b1==0)and(i%c1==0):
        print(i)
        break
