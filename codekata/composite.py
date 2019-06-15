u=int(input())
if u>0:
  for x in range(2,u):
    if(u%x==0):
      print("yes")
      break
  else:
      print("no")
else:
  print("no")
