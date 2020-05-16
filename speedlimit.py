while True:
    num_inputs = int(input())
    if num_inputs == -1:
        break
    miles = 0
    last_time = 0
    for i in range(num_inputs):
        line = list(map(int, input().split()))
        miles += line[0] * (int(line[1]) - last_time)
        last_time = line[1]
    print(str(miles) + " miles")
