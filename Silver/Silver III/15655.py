def backtrack(depth):
  if depth == m:
    if result == sorted(result):
      print(*result)
    return

  for i in range(n):
    if arr[i] in result:
      continue
    result.append(arr[i])
    backtrack(depth + 1)
    result.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []
backtrack(0)
