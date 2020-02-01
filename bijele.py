found_pieces = list(map(int, input().split()))
required_pieces = [1, 1, 2, 2, 2, 8]

for i in range(len(required_pieces)):
    print(required_pieces[i] - found_pieces[i], end = " ")