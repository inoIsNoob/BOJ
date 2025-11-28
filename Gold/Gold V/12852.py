x = int(input())
d = [0] * (10**6 + 1)

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
print(d[x])

print(x,end=' ')
while x != 1:
  did = False
  if x % 2 == 0:
    if d[x//2] == d[x]-1:
      print(x//2, end=' ')
      x = x//2
      did = True
  if x % 3 == 0:
    if d[x//3] == d[x]-1:
      print(x//3, end=' ')
      x = x//3
      did = True
  if not did:
    print(x-1, end=' ')
    x -= 1
    did = False
