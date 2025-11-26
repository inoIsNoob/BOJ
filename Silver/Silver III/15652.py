def beNormal(output):
  for i in range(1, m):
    if output[i] == n:
      output[i-1] += 1
      output[i] = output[i-1]-1

n, m = map(int, input().split())
output = [1 for _ in range(m)]

print(*output)
if not(n==m==1):
  while True:
    output[-1] += 1
    print(*output)
    if output.count(n) == m:
      break
    beNormal(output)
