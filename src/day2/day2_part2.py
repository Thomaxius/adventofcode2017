import itertools

input = open("input.txt")
input = input.read()
input = input.split('\n')

def solve(input):
    sum = 0
    for row in input:
        row = row.split('\t')
        for a, b in itertools.combinations(row, 2):
            result = compare(int(a),int(b))
            if result:
                sum += result
    return int(sum)


def compare(a, b):
    bigger = max([a,b])
    smaller = min([a,b])
    return bigger / smaller if not bigger%smaller else None

print(solve(input))
