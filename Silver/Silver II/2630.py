def makePaper(graph, length):
    global cntB; global cntW
    
    if isSame(graph, length):
      if graph[0][0]:
        cntB += 1
      else:
        cntW += 1
      return

    k = length // 2
    div1 = [graph[x][-k:] for x in range(k)]
    div2 = [graph[x][:k] for x in range(k)]
    div3 = [graph[x+k][:k] for x in range(k)]
    div4 = [graph[x+k][-k:] for x in range(k)]
    for i in (div1, div2, div3, div4):
      makePaper(i, k)

def isSame(graph, length):
    std = graph[0][0]
    for i in range(length):
      for j in range(length):
        if graph[i][j] != std:
          return False
    return True

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
cntB, cntW = 0, 0
makePaper(graph, n)
print(cntW)
print(cntB)
