C = float(input())
L = int(input())
total_area = 0

for i in range(L):
    dimensions = list(map(float, input().split()))
    total_area += dimensions[0] * dimensions[1]

print("%.8f" % (C * total_area))
