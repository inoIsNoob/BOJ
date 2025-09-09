xa,ya,xb,yb,xc,yc = map(int, input().split())
if xb-xa == 0:
    slopeAB = float('inf')
else:
    slopeAB = (yb-ya)/(xb-xa)

if xc-xa == 0:
    slopeAC = float('inf')
else:
    slopeAC = (yc-ya)/(xc-xa)

if slopeAB == slopeAC:
    print(-1.0)
else:
    #선분 AB
    AB = ((yb-ya)**2 + (xb-xa)**2)**0.5
    #선분 BC
    BC = ((yc-yb)**2 + (xc-xb)**2)**0.5
    #선분 AC
    AC = ((yc-ya)**2 + (xc-xa)**2)**0.5
    
    scale = sorted([AB,BC,AC])
    result = 2*(scale[2] + scale[1]) - 2*(scale[0] + scale[1])
    print(result)
