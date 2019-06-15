Str=list(input())
if len(Str)%2==0:
    Str[int(len(Str)/2)] ='*'
    Str[int(len(Str)/2)-1]='*'
else:
    Str[int(len(Str)/2)] ='*'
for i in range(0,len(Str)):
    print(Str[i],end='')
