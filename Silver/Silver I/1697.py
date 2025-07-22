n, k = map(int, input().split())
visited = [False] * 100001
d = [[] for _ in range(100001)]
d[0] += [n]
for i in range(1, 100001):
  for j in d[i-1]:
    for x in (j+1, j-1, j*2):
      if x>100000 or x<0: continue
      if not visited[x]:
        visited[x] = True
        d[i] += [x]
  if k in d[i]:
    break

if n > k:
  print(n-k)
elif n == k:
  print(0)
else:
  print(i)
