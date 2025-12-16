prime = [True for x in range(int(1e7)+1)]
prime[0] = prime[1] = False
a,b=map(int,input().split())
for i in range(2, int(1e7)+1):
    if prime[i]:
      for j in range(i*i, int(1e7)+1, i):
        prime[j] = False

cnt = 0

for i in range(2, int(1e7)+1):
  if prime[i]:
    tmp = i*i
    while tmp <= b:
      if tmp >= a:
        cnt += 1
      tmp *= i

print(cnt)
