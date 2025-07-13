n = int(input())
d = list(map(int, input().split()))

days = []
idx = 0
res = 0
for i in range(1, 365+1):
  if idx >= n:
    break
  if i == d[idx]:
    idx += 1
    days += [0]
  
  days = [x + 1 for x in days]

  if sum(days) >= 20:
    days.clear()
    res += 1

if days:
  res += 1

print(res)
