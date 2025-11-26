a, b = input().split()
cnt = 1
while True:
  cnt += 1

  if b[-1] == '1':
    b = b[:-1]
  else:
    if int(b)%2 == 0:
      b = str(int(b)//2)
    else:
      result = -1
      break
  
  if int(b) < int(a):
    result = -1
    break
  
  if b == a:
    result = cnt
    break

print(result)
