n = int(input())
w = int(input())
result = n * 10
if n >= 3: result += 20
if n == 5: result += 50
if w > 1000: result -= 15

print(result if result > 0 else 0)
