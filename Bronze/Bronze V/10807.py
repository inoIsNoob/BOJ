amount = int(input())
if amount != 0:
  nums = list(map(int, input().split()))
  found = int(input())
  print(nums.count(found))
