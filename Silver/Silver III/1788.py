n = int(input())
d = [0] * (1000000+1)
d[1] = 1
for i in range(2, abs(n)+1):
  d[i] = (d[i-1] + d[i-2]) % 1000000000

if n == 0:
  print(0)
elif n > 1:
  print(1)
else:
  if n % 2 == 1:
    print(1)
  else:
    print(-1)

print(d[abs(n)] % 1000000000) 
