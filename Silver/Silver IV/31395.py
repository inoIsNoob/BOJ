n = int(input())
a = list(map(int, input().split()))

k, i, res = 0, 0, 0
while True:
  res += i+1
  i += 1
  if k+i >= n:
      break
  if a[k + i-1] > a[k + i]:
    k, i  = k+i, 0

print(res)
