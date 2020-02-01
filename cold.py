days = int(input())
temperature = list(map(int, input().split()))
result = 0;

for i in range(days):
    if temperature[i] < 0: result += 1
    
print(result)