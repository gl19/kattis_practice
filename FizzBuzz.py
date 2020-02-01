x = list(map(int, input().split()))
fizz = x[0]
buzz = x[1]
n = x[2] + 1

for i in range(1, n):
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz")
    elif i % fizz == 0:
        print("Fizz")
    elif i % buzz == 0:
        print("Buzz")
    else:
        print(i)