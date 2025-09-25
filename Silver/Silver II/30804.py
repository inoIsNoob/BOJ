n = int(input())
S = list(map(int, input().split()))
cnt = [0] + [0 for _ in range(9)]
start, end = 0, 0
maxLength = 0

while end < n:
    if cnt.count(0) == 7:
        cnt[S[start]] -= 1
        maxLength = max(maxLength, end-start-1)
        start += 1
        continue
    cnt[S[end]] += 1
    end += 1

if cnt.count(0) != 7:
    print(max(maxLength, len(S[start:end])))
else:
    print(maxLength)
