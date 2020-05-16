x = list(map(int, input().split()))
list = [0] * (x[0] + x[1])
max = 0

for i in range(x[0]):
    for j in range(x[1]):
        list[i + j + 1] += 1
        if list[i + j + 1] > max:
            max = list[i + j + 1]
            
for i in range(len(list)):
    if list[i] == max:
        print(i + 1)
        