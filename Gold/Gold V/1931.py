n = int(input())

times = dict()
for _ in range(n):
    v, k = map(int, input().split())
    if k in times:
        times[k] += [v]
        times[k] = sorted(times[k])
    else:
        times[k] = [v]
times = sorted(times.items())

conf = list()
for k in times:
    for i in k[1]:
        conf.append([i, k[0]])

endTime = conf[0][1]
cnt = 1
for i in range(1, n):
    if conf[i][0] >= endTime:
        endTime = conf[i][1]
        cnt += 1

print(cnt)
