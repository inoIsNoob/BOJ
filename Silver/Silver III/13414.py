k, l = map(int, input().split())
success = {}
canAttend = 0
for _ in range(l):
  studentID = input()
  if success.get(studentID) == 1:
    del success[studentID]
  success[studentID] = 1

for stdt in success:
  canAttend += 1
  print(stdt)
  if canAttend == k:
    break
