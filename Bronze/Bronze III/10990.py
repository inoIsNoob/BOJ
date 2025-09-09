a = int(input())
    
print(" "*(a-1),end="*")
print()
for i in range(0, a-1):
    print(" "*(a-i-2),end="*")
    print(" "*(2*i + 1), end="*")
    print()
