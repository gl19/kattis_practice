x = int(input())
for i in range(x):
    y = int(input())
    places = []
    for j in range(y):
        places.append(str(input()))
    print(len(set(places)))