n = int(input())

scores = [0]
for _ in range(n):
  scores.append(int(input()))

d = [0] * (n+1)

if n >= 1:
  d[1] = scores[1]
if n >= 2:
  d[2] = scores[1] + scores[2]
for i in range(3, n + 1):
  d[i] = max(d[i - 2] + scores[i],
             d[i - 3] + scores[i - 1] + scores[i]) 

print(d[-1])
