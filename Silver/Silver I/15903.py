n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards = sorted(cards)
    cards[0], cards[1] = cards[0]+cards[1], cards[1]+cards[0]

print(sum(cards))
