n, m = map(int,input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
part_sum = 0
result = 0
while end < n:
  part_sum += arr[end] 
  while part_sum > m:
    part_sum -= arr[start]
    start += 1
  if part_sum == m:
    result += 1
  
  end += 1
