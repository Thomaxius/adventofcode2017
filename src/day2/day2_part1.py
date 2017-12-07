input = open("input.txt")
input = input.read()
input = input.split('\n')

def solve(input):
    sum = 0
    for row in input:
        row = row.split('\t')
        max = 0
        min = None
        for item in row:
            item = int(item)
            if item > max:
                max = item
            if min == None:
                min = item
            if item < min:
                min = item
        sum += max - min
    return sum

print(solve(input))
