from collections import deque

n = int(input())
lines = deque()
for _ in range(n):
    lines.append(list(map(int, input().split())))

if n == 1:
    std = [0, 0]
else:
    i = 0
    std = lines.popleft()
    while True:
        if (std[0] <= lines[0][0] <= std[1]) or (std[0] <= lines[0][1] <= std[1]) or (std[0] > lines[0][0] and std[1] < lines[0][1]):
            std[0], std[1] = min(lines[0][0], std[0]), max(lines[0][1], std[1])
            lines.popleft()
            i = 0
        else:
            lines.append(std)
            std = lines.popleft()
        i += 1
        if i == len(lines)+1:
            break

answer = list(lines) + [std]
print(sum(y-x for x,y in answer))
