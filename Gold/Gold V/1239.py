from itertools import permutations

n = int(input())
portion = list(map(int, input().split()))

result = 0
for p in permutations(portion):
  sum_set = set()
  temp = 0
  for x in p:
    temp += x
    sum_set.add(temp)
  
  cnt = 0
  for i in sum_set:
    if i+50 in sum_set:
      cnt += 1
  
  result = max(result, cnt)

print(result)
