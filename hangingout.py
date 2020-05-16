first_line = list(map(int, input().split()))
L = first_line[0]
x = first_line[1]
num_people = 0
cases_denied = 0

for i in range(x):
    case = list(map(str, input().split()))
    if case[0] == "enter":
        if num_people + int(case[1]) > L:
            cases_denied += 1
        else:
            num_people += int(case[1])
    else:
        num_people -= int(case[1])

print(cases_denied)
