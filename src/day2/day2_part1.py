input = open("input.txt")
input = input.read()
input = input.split('\n')

def solve(input):
    sum = 0
    for row in input:
        row = row.split('\t')
        max = 0
        min = None
        for digit in row:
            digit = int(digit)
            if digit > max:
                max = digit
            if min == None:
                min = digit
            if digit < min:
                min = digit
                print(min)
        sum += max - min
    return sum

print(solve(input))
