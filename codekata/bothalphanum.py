s=input()
letter_flag = False
number_flag = False
for a in s:
  if a.isalpha():
      letter_flag = True
  if a.isdigit():
      number_flag = True
if letter_flag and number_flag:
      print('Yes')
else:
  print('No')
