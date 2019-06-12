k=int(input())
if((k%4==0) and (k%100!=0)):
  print('yes')
elif(k%400==0):
  print('yes')
else:
  print('no')
