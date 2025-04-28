import sys
input=sys.stdin.readline

a=[1 for x in range(1000000)]
a[0]=a[1]=0
for i in range(2, int(1000000**0.5) + 1):
  if not a[i]:
    continue
  for j in range(2*i, 1000000, i):
    a[j]=0

while True:
  n=int(input())
  if n==0: break

  buff=3;
  while True:
    if a[n-buff]==a[buff] and a[buff]==1:
      print(f'{n} = {buff} + {n-buff}')
      break
    buff+=2
  else:
    print("Goldbach's conjecture is wrong.")
