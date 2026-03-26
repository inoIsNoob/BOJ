r, s = map(int, input().split())
picture = [list(input()) for _ in range(r)]
stone = [-1] * s
ground = [3000] * s
for i in range(r):
  for j in range(s):
    if picture[i][j] == 'X':
      stone[j] = max(i, stone[j])
    if picture[i][j] == '#':
      ground[j] = min(i, ground[j])

touch = 3000
for i in range(s):
  if stone[i] > -1:
    touch = min(ground[i] - stone[i], touch)
touch -= 1

for i in range(r-1, -1, -1):
  for j in range(s):
    if picture[i][j] == 'X':
      picture[i][j], picture[i+touch][j] = picture[i+touch][j], picture[i][j]

for k in picture:
  print(*k)
