def solve(input):

    input = input.rstrip('\n').split('\n')
    comparsion_list = []
    i = 0
    for row in input:
        wordlist = row.split()
        for word in wordlist:
            comparsion_list.append(''.join(sorted(word)))
        if len(wordlist) == len(set(comparsion_list)):
            i += 1
        comparsion_list = []
    return i

input = open("input.txt")
input = input.read()
print(solve(input))

