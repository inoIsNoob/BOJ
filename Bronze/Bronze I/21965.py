def isMountain(arr):
  for i in range(len(arr)-1):
    if arr[i] >= arr[i + 1]:
      return False
  return True

n = int(input())
a = list(map(int, input().split()))
right, left = a[:a.index(max(a))], a[a.index(max(a)):]
if isMountain(right) and isMountain(list(reversed(left))) and a.count(max(a)) == 1:
  print('YES')
else:
  print('NO')
