n = int(input())
picked = list(map(int, input().split()))

res = []
for i in range(n):
  if not picked[i]:
    res.append(i+1)
  else: 
    res.insert(-picked[i], i+1)

print(*res)
