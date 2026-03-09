def calc_footstep():
  footstep = 0
  for i in range(1, 20):
    for j in range(i-1, -1, -1):
      if height[i] < height[j]:
        footstep += 1
  
  return footstep

T = int(input())
total = 0

for c in range(T):
  s = list(map(int, input().split()))
  height = s[1:]
  total = calc_footstep()
  print(c+1, total)
