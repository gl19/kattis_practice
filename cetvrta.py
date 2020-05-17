x_coordinates = []
y_coordinates = []

for i in range(3):
    coordinate = list(map(int, input().split()))
    x_coordinates.append(coordinate[0])
    y_coordinates.append(coordinate[1])

x = 0
y = 0
for i in range(3):
    if x_coordinates.count(x_coordinates[i]) == 1:
        x = x_coordinates[i]
    if y_coordinates.count(y_coordinates[i]) == 1:
        y = y_coordinates[i]
    
print(str(x) + " " + str(y))