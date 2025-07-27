n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

minSec, maxHeight = float('inf'), 0

for h in range(0, 257):
  sec = 0
  block = b
  for i in range(n):
    for j in range(m):
      diff = ground[i][j] - h
      if diff > 0:
        sec += diff * 2
        block += diff
      elif diff < 0:
        sec += (-diff) * 1
        block -= (-diff)
  
  if block < 0: continue

  if sec < minSec:
    minSec = sec
    maxHeight = h
  elif sec == minSec:
    maxHeight = max(h, maxHeight)

print(minSec, maxHeight)
