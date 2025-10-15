result = 0
for _ in range(int(input())):
    a = input()
    result = max(result, a.count('for')+a.count('while'))

print(result)
