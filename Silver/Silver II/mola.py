from collections import deque

n = 8#int(input())
goal = ['4','3','6','8','7','5','2','1']
seq = deque()
for j in range(n):
    seq.append(str(j+1))
box = deque()
gi=0
before = False

while True:
    if before:
        num = box.pop()
    else:
        num = seq.popleft()
    
    if goal[gi] != num:
        if not before:
            print('+')
        before = False
        box.append(num)
    else:
        if before:
            print('-')
        else:
            print('+'); print('-')
        gi += 1
        before=True
