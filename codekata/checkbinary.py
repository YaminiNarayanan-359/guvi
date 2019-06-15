t=input()
s=0
for i in t:
  if((i=='0')|(i=='1')):
    s=s+1
if(s==len(t)):
  print('yes')
else:
  print('no')
