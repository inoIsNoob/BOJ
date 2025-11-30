na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
yes_dict = {}
result = []
for i in b:
  yes_dict[i] = 1

for i in a:
  if not yes_dict.get(i):
    result.append(i)

print(len(result))
if result:
  print(*sorted(result))
