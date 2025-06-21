mode = dict()

for _ in range(int(input())):
  info = input().split()
  a = info[2:]
  for i in a:
    if i not in mode:
      mode[i] = 1
    else:
      mode[i] += 1

chk = sorted(list(mode.values()))
res = {v:k for k,v in mode.items()}
if len(chk) == 1:
  print(res[max(res)])
else:
  if chk[-1] == chk[-2]:
    print(-1)
  else:
    print(res[max(res)])
