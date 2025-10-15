n = int(input())
winner = [0, 50, 180, 0]
for i in range(n):
    s, c, l = map(int, input().split())
    if s > winner[0]:
        winner = [s, c, l, i+1]
    elif s == winner[0]:
        if c < winner[1]:
            winner = [s, c, l, i+1]
        elif s == winner[1]:
            if l < winner[2]:
                winner = [s, c, l, i+1]

print(winner[-1])
