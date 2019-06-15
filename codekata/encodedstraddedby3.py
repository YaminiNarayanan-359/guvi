p=input()
q=[]
for i in p:
    a=65+(ord(i)-65+3)%26
    q.append(chr(a))
print("".join(q))
