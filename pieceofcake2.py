x = list(map(int, input().split()))
if x[1] > x[0]/2:
    print(x[1] * x[2] * 4) if x[2] > x[0]/2 else print(x[1] * (x[0] - x[2]) * 4)
else:
    print((x[0] - x[1]) * x[2] * 4) if x[2] > x[0]/2 else print((x[0] - x[1]) * (x[0] - x[2]) * 4)