n = input()
m = int(input())
broken = set()
if m > 0: broken = set(input().split())

result = abs(100-int(n))
for channel in range(1000001):
  flag = True
  for char in str(channel):
    if char in broken:
      flag = False
      break
  
  if flag:
    press = len(str(channel)) + abs(channel - int(n))
    result = min(result, press)

print(result)
