n, k = map(int, input().split())
arr = [0, 1] + [x for x in range(2, n+1)]
cnt = 0
for i in range(2, n+1):
  if cnt == k:
    break
  for j in range(1, n):
    if i*j > n:
      break
    if arr[i*j] != 0:
      result = arr[i*j]
      arr[i*j] = 0
      cnt += 1
    if cnt == k:
      break

print(result)
