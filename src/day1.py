def solve(input):
    input = str(input)
    sum = 0
    i = 0
    for x in input:
        if input[i] == input[-1] and (i == len(input)-1):
            if input[-1] == input[0]:
                sum += int(input[-1])
            break
        if input[input.find(x,i)] == input[input.find(x,i)+1]:
            sum += int(input[input.find(x,i)])
        i += 1
    return sum

def test():
    tests = [
    solve('1122') == 3,
    solve('1111') == 4,
    solve('1234') == 0,
    solve('91212129') == 9,
    ]
