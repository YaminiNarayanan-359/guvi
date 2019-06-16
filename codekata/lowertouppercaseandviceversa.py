l=list(map(str,input()))
for i in range(len(l)):
    if l[i].islower()==True:
        l[i]=l[i].capitalize()
    else:
        l[i]=l[i].lower()
for i in range(len(l)):
   print(l[i],end="")
