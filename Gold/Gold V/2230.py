n,m=map(int, input().split())
a = list()
for _ in range(n):
  a.append(int(input()))
a = sorted(a)

start, end = 0, 0
result = 1e10
while end < n:
  if a[end] - a[start] < m:
    end += 1
  elif a[end] - a[start] > m:
    result = min(result, a[end] - a[start])
    start += 1
  else:
    result = m
    break

print(result)
