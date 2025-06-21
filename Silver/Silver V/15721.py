a = int(input())
t = int(input())
slogan = input()

x, order, cnt = 0, -1, 0
while cnt != t:
  x += 1
  bundegi = '0101' + '0'*(x+1) + '1'*(x+1)
  for i in bundegi:
    order += 1
    if order == a:
      order = 0

    if i == slogan:
      cnt += 1
      if cnt == t:
        break
  
print(order)
