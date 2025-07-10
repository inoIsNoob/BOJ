import heapq, sys
input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
  var = int(input())
  if var == 0:
    try:
      print(heapq.heappop(heap))
    except:
      print(0)
  else:
    heapq.heappush(heap, var)
