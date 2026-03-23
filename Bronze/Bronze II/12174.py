def two_to_deci(bit, binery):
  char = ''
  for i in range(bit):
    result = 0
    for j in range(8):
      if binery[i*8 + j] == "I":
        result += 2**(7-j)
    char += chr(result)
  
  return char

t = int(input())
for rp in range(t):
  b = int(input())
  binery = input()
  print(f'Case #{rp+1}: {two_to_deci(b, binery)}')
