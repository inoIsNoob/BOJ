from collections import deque

low = deque([97+x for x in range(26)])
up = deque([65+x for x in range(26)])

k, s = map(int, input().split())
ststst = input()
low.rotate(-k)
up.rotate(-k)

for char in ststst:
  if char == ' ' or char == ',' or char == '.':
    print(char, end='')
    continue

  if char.isupper():
    print(chr(up[ord(char) - 65]), end='')
  else:
    print(chr(low[ord(char) - 97]), end='')
