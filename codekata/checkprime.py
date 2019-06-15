h=int(input())
if h>0:
  for x in range(2,h):
    if(h%x==0):
      print("no")
      break
  else:
      print("yes")
else:
  print("no")
