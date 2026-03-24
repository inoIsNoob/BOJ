n = int(input())
idx = 0
goal = '2023'
result = 0

for i in range(2023, n+1):
  for char in str(i):
    if char == goal[idx]:
      idx += 1
    if idx == 4:
      idx = 0
      result += 1
      break
  idx = 0

print(result)
