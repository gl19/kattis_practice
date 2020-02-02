mb_per_month = int(input())
num_of_months = int(input())
total_mb = mb_per_month * (num_of_months + 1)

for i in range(num_of_months):
    total_mb -= int(input())
    
print(total_mb)