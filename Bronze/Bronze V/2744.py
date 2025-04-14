import sys
input = sys.stdin.readline

myStr = input()

for i in myStr:
  if i.isupper() == True:
    print(i.lower(),end='')
  else:
    print(i.upper(),end='')
