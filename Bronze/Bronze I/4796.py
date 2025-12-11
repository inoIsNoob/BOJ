i = 0
while True:
  i += 1
  result = 0
  l, p, v = map(int, input().split())
  if l==p==v==0: break
  result += (v//p) * l
  if l > v%p:
    result += v%p
  else:
    result += l
  print(f'Case {i}: {result}')
