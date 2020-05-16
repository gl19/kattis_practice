num_bats = int(input())
results = list(map(int, input().split()))
runs = 0
num_walks = 0

for i in range(num_bats):
    result = results[i]
    if result == -1:
        num_bats -= 1
    else:
        runs += result

print(runs / num_bats)
