n = input()
n_numlize = sorted([int(i) for i in n], reverse=True)
if int(n) >= 30 and sum(n_numlize) % 3 == 0 and n_numlize[-1] == 0:
  for i in n_numlize:
    print(i,end='')
else:
  print(-1)
