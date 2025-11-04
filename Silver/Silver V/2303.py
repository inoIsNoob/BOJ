n = int(input())
maxValue = 0
for order in range(n):
    cards = list(input().split())
    cards = [int(str(x)[-1]) for x in cards]
    for i in range(0, 3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                sumBack = int(str(cards[i]+cards[j]+cards[k])[-1])
                if sumBack >= maxValue:
                    winner = order + 1
                    maxValue = sumBack

print(winner)
