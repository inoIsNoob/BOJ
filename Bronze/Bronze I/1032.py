tmp = ''; indexQ = list()
for _ in range(int(input())):
  fileName = input()
  if tmp == '':
    tmp = fileName
    continue
  for i in range(len(tmp)):
    if fileName[i] != tmp[i]:
      indexQ += [i]

result = ''
for j in range(len(tmp)):
  result += fileName[j] if j not in indexQ else '?'

print(result)
