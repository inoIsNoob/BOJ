from collections import deque

for _ in range(int(input())):
    team = 0
    n = int(input())
    num = [None] + list(map(int, input().split()))
    alTeam = [0] + [0 for _ in range(n)]
    for i in range(1, n+1):
        q = deque([i])
        if not alTeam[i]:
            while q:
                x = q[-1]
                alTeam[x] = 1
                if alTeam[num[x]] == 2:
                    for j in q:
                        alTeam[j] = 2
                    break
                if alTeam[num[x]] == 1:
                    member = len(q) - q.index(num[x])
                    team += member
                    for j in q:
                        alTeam[j] = 2
                    break
                q.append(num[x])
    print(n - team)
