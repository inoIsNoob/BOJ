def solveEquation(a, b, c):
  k = b**2 - 4*a*c
  print(f'{(-b + k**0.5) / (2*a):.3f}, {(-b - k**0.5) / (2*a):.3f}')

for _ in range(int(input())):
  a, b, c = map(float, input().split())
  solveEquation(a, b, c)
