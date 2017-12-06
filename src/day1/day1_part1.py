def solve(input):
    input = str(input)
    sum = 0
    i = 0
    steps = int(len(input)/2)
    for x in input:
        if (i + steps) >= len(input):
            if input[i] == input[(i+steps)-(len(input))]:
                sum += int(input[i])
            i += 1
            continue
        if input[input.find(x,i)] == input[input.find(x,i)+int(steps)]:
            sum += int(input[input.find(x,i)])
        i += 1
    return sum

def test():
    tests = [
    solve('1212') == 6,
    solve('1221') == 0,
    solve('123425') == 4,
    solve('123123') == 12,
    solve('12131415') == 4
    ]
    print(tests)
