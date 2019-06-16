d1=input().split()
d2=input().split()
d3=input().split()
if(d1[0]==d2[0]==d3[0] or d1[1]==d2[1]==d3[1] or (d1[0]==d1[1] and d2[0]==d2[1] and d3[0]==d3[1])):
    print('yes')
else:
    print('no')
