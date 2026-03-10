def condition1(s):
  return 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s

def condition2(s):
  bool_s = [1 if x in 'aeiou' else 0 for x in s]
  now = bool_s[0]
  cnt = 1
  for i in range(1, len(s)):
    if now == bool_s[i]:
      cnt += 1
    else:
      cnt = 1
      now = bool_s[i]

    if cnt == 3:
      return False
  return True

def condition3(s):
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      if s[i] != 'e' and s[i] != 'o':
        return False
  return True

while True:
  t = input()
  if t == 'end': break
  if condition1(t) and condition2(t) and condition3(t):
    print(f'<{t}> is acceptable.')
  else:
    print(f'<{t}> is not acceptable.')
