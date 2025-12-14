def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

for _ in range(int(input())):
  result = 0
  size, *arr = map(int, input().split())
  for i in range(size-1):
    for j in range(i+1, size):
      result += gcd(arr[i], arr[j])

  print(result)
