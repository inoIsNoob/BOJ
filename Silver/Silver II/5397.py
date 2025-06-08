from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  log = list(input().rstrip())
  password = deque()
  cursor = 0
  for i in log:
    if i == '<':
      if cursor > 0:
        cursor -= 1
    elif i == '>':
      if cursor < len(password):
        cursor += 1
    elif i == '-':
      if not password or cursor == 0:
        continue
      del password[cursor - 1]
      cursor -= 1
    else:
      password.insert(cursor, i)
      cursor += 1
  print(''.join(password))
