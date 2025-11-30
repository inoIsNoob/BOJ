n = int(input())
minus, plus = [], []
zero, one, mone = 0, 0, 0
# 음, 양은 정수범위이므로 배열, -1, 0, 1은 갯수로 할당
complete = [] #묶어서 계산된 수 넣을거
for _ in range(n):
  num = int(input())
  if num == -1:
    mone += 1
  elif num == 0:
    zero += 1
  elif num == 1:
    one += 1
  elif num < 0:
    minus.append(num)
  elif num > 0:
    plus.append(num)

minus = sorted(minus, reverse=True)
plus = sorted(plus)
# 음수 처리
while len(minus) > 1:
  complete.append(minus[-1] * minus[-2])
  minus.pop(); minus.pop()
  # print(complete, '음수 처리')
# 양수 처리
while len(plus) > 1:
  complete.append(plus[-1] * plus[-2])
  plus.pop(); plus.pop()
  # print(complete, '양수 처리')
# 마일 처리
if mone > 0 and minus:
  complete.append(-minus.pop())
  mone -= 1
complete.append(mone//2)
mone = mone%2
# print(complete, mone, '마일 처리')
# 제로 처리
if zero > 0 and minus:
  minus.pop()
  zero -= 1
if zero >0 and mone:
  mone = 0
# print(complete, zero, '제로 처리')
complete.append(-mone)
complete.append(one)
complete += minus
complete += plus
# print(complete)
print(sum(complete))
