n, m = map(int, input().split())
castle = [input() for _ in range(n)]

rowNeed, colNeed = 0, 0
for i in range(n):
  if castle[i].count(".") == m:
    rowNeed += 1
for i in range(m):
    rotateCastle = [x[i] for x in castle]
    if rotateCastle.count(".") == n:
      colNeed += 1

print(max(rowNeed, colNeed))
