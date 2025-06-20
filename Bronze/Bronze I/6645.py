while True:
  n, issue = input().split()
  if n == '0' and issue == 'END': break

  buyer, seller, info = dict(), dict(), dict()
  for _ in range(int(n)):
    name, option, price = input().split()
    info[name] = []
    if option == 'buy':
      buyer[name] = float(price)
    elif option == 'sell':
      seller[name] = float(price)

  for i in buyer:
    for j in seller:
      if buyer[i] >= seller[j]:
        info[i] += [j]
        info[j] += [i]
  
  print(issue)
  for i in info:
    print(i,end=': ')
    if not info[i]:
      print('NO-ONE')
      continue
    print(*info[i])
