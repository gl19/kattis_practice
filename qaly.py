x = int(input())
qaly = 0
for i in range(x):
    a = list(map(float, input().split()))
    qaly += a[0] * a[1]
print(qaly)