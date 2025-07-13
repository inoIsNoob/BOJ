spendTime = 0
for _ in range(4):
  spendTime += int(input())

if spendTime + 300 <= 1800: print('Yes')
else: print('No')
