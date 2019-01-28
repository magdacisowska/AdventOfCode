input = open('inputs/input77.txt').read().splitlines()

rules = {}

for line in input:
    _, before, _, _, _, _, _, after, _, _ = line.split(' ')
    rules[before] = rules.get(before, '') + after

# sort alphabetically
for before, after in rules.items():
    rules[before] = sorted(after)
print('Rules: ', rules)

next_step = input[0][5]
end_step = 'E'

# a list representing the solution
order = [next_step]

# que for waiting symbols
Q = []

i = 0

while i < 7:

    print(rules.get(next_step))

    if rules.get(next_step) is not None:
        order.append(rules.get(next_step)[0])
        if rules.get(next_step)[1:]:
            Q.append(rules.get(next_step)[1:])
        next_step = rules.get(next_step)[0]

    else:
        next_step = Q.pop()
        order.pop()

    i += 1

print(order)
