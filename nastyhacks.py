a = int(input())
for i in range(a):
    x = list(map(int, input().split()))
    if x[0] + x[2] < x[1]:
        print("advertise")
    elif x[0] + x[2] == x[1]:
        print("does not matter")
    else:
        print("do not advertise")