inputs = list(input().split())

if inputs[0] == '0' and inputs[1] == '0':
    print("Not a moose")
elif inputs[0] == inputs[1]:
    print("Even " + str(2 * int(inputs[1])))
else:
    print("Odd " + str(2 * max(int(inputs[0]), int(inputs[1]))))
