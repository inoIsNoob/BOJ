from collections import deque

for _ in range(int(input())):
  p = input()
  n = int(input())
  x = deque(eval(input()))
  switch = 0 #짝수면 앞, 홀수면 뒤
    
  error = False
  for i in p:
    if i == 'R':
      switch += 1
    elif i == 'D':
      if not x:
        error = True
        break

      if switch%2 == 0:  x.popleft()
      else:              x.pop()
        
  if error:
    print('error')
  else:
    if switch%2 == 0:  x = map(str, x)
    else:              x = map(str, reversed(x))
    print('[' + ','.join(x) + ']')
