j,k= map(int,input().split())
k= k%j
s1 = list(map(int,input().split()))
s2 = s1[-k:] + s1[:-k]
print(*s2)
