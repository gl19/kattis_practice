x = list(map(int, input().split()))
matches = x[0]
width = x[1]
height = x[2]

for i in range(matches):
    if int(input()) ** 2 <= (width ** 2 + height ** 2):
        print("DA")
    else:
        print("NE")