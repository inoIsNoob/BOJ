x, y = [], []
n = int(input())
RSS = 0
for _ in range(n):
  xi, yi = map(int, input().split())
  x.append(xi)
  y.append(yi)

small = 1e9
for a in range(1, 101):
  for b in range(1, 101):
    RSS = 0
    for i in range(n):
      RSS += (y[i] - (a*x[i] + b))**2
    
    if small > RSS:
      small = RSS
      then = (a, b)

print(*then)
