h=input()
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=['a','e','i','o','u']
if(h in l1):
  if(h in l2):
    print('Vowel')
  else:
    print('Consonant')
else:
  print('invalid')
