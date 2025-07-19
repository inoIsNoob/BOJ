origin = "SciComLove"
S = input()

res = 0
for i in range(10):
    if origin[i] != S[i]:
        res += 1

print(res)
