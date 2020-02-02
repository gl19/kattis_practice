a = int(input())
for i in range(a):
    x = int(input())
    print(str(x) + " is odd") if x % 2 == 1 else print(str(x) + " is even")