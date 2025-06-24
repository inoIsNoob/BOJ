n, m = map(int, input().split())

Spack, Seach = 1000, 6000
for _ in range(m):
    pack, each = map(int, input().split())
    Spack = min(Spack, pack)
    Seach = min(Seach, each)

onlyPack = (n//6 + (1 if n%6 != 0 else 0))*Spack
mixed = (n//6)*Spack + (n%6)*Seach
onlyEach = n * Seach

print(min(onlyPack, mixed, onlyEach))
