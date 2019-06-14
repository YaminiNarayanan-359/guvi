t,v=input().split()
if(len(t)>len(v)):
  print(t)
elif(len(v)>len(t)):
  print(v)
elif(len(t)==len(v)):
  print(t or v)
