whatNeed = [0 for _ in range(6)]
wPiece = list(map(int, input().split()))

for i in range(6):
  if i <= 1:
    if wPiece[i] != 1:
      whatNeed[i] = 1 - wPiece[i]
  elif 1 < i <= 4:
    if wPiece[i] != 2:
      whatNeed[i] = 2 - wPiece[i]
  else:
    if wPiece[i] != 8:
      whatNeed[i] = 8 - wPiece[i]

for j in range(6):
  print(whatNeed[j])
