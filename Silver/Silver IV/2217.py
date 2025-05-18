import sys
input = sys.stdin.readline

n = int(input())
t = list()
for _ in range(n):
  t.append(int(input()))
t.sort()
arr=[]
for i in range(n):
  arr.append(t[i] * (n-i))

print(max(arr))
