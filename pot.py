x = []
sum = 0
inputs = range(int(input()))

for i in inputs:
    x.append(input())

for i in inputs:
    sum += int(x[i][:-1]) ** int(x[i][-1:])

print(sum)
