n, m = map(int, input().split())
idol = {}

for _ in range(n):
  teamName = input()
  idol[teamName] = []
  groupNumber = int(input())
  for _ in range(groupNumber):
    member = input()
    idol[teamName].append(member)
    idol[member] = teamName

for _ in range(m):
  quiz = input()
  genre = int(input())
  if genre == 1:
    print(idol[quiz])
  elif genre == 0:
    for i in sorted(idol[quiz]):
      print(i)
