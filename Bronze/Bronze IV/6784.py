n = int(input())
choice, answer = list(), list()
result = 0

for _ in range(n):
    choice.append(input())

for _ in range(n):
    answer.append(input())

for i in range(n):
    if choice[i] == answer[i]: result += 1

print(result)
