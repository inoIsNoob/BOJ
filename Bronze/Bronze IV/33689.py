n = int(input())
res = 0
for _ in range(n):
    cand = input()
    if cand[0] == 'C':
        res += 1

print(res)
