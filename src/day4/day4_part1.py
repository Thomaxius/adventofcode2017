def solve(input):
    input = input.split('\n')
    cleaned = [row for row in input if not (len(row.split(' ')) > len(set(row.split(' '))))]
    return len(cleaned)

input = open("input.txt")
input = input.read()
print(solve(input))

