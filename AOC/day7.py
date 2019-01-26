import collections

input = open('inputs/input77.txt').read().splitlines()

rules = {}

for line in input:
    _, before, _, _, _, _, _, after, _, _ = line.split(' ')
    rules[before] = rules.get(before, '') + after

for before, after in rules.items():
    rules[before] = sorted(after)

# rules = collections.OrderedDict(sorted(rules.items()))
print(rules)

next_step = input[0][5]
# print(next_step)

order = [next_step]

while len(order) != len(rules):

    print(next_step, order)

    if rules.get(next_step, None):
        next_step = rules.get(next_step, None)[0]

        values = rules.get(next_step)
        if values is not None:
            values = (list(reversed(values)))
            values.pop()
            values = (list(reversed(values)))
            print(values)
            # rules[next_step] = values

        order.append(next_step)
    else:
        order.pop()
        next_step = order[-2]

print(rules)