def solve(input):
    input = input.rstrip('\n')
    return len([row for row in input.split('\n') if not (len(row.split(' ')) > len(set(row.split(' '))))])

input = open("input.txt")
input = input.read()
print(solve(input))

