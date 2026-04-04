n = int(input())
street = list(map(int, input().split()))
Lcost = list(map(int, input().split()))
Lcost.pop()

result, cpst = 0, 1e9
for i in range(n-1):
  cpst = min(cpst, Lcost[i])
  result += street[i] * cpst

print(result)
