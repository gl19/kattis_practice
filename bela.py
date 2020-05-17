first_line = list(input().split())
N = first_line[0]
B = first_line[1]
total = 0

for i in range(int(N) * 4):
    card = input()
    num = card[0]
    suit = card[1]
    if num == 'A':
        total += 11
    elif num == 'K':
        total += 4
    elif num == 'Q':
        total += 3
    elif num == 'J':
        if suit == B:
            total += 20
        else:
            total += 2
    elif num == 'T':
        total += 10
    elif num == '9':
        if suit == B:
            total += 14

print(total)
