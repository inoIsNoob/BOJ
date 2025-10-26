n = int(input())
for i in range(n):
    word = list(reversed(input().split()))
    print(f"Case #{i+1}:",*word)
