n,s =map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
part_sum = 0
result = float('inf')

while end < n:
  part_sum += arr[end]

  while part_sum >= s:
    result = min(result, end - start + 1)
    part_sum -= arr[start]
    start += 1
        
  end += 1
    
if result == float('inf'):
  print(0)
else:
  print(result)
