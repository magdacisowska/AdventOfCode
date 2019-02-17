def parse(data, index):
    num_leaves = int(data[index])
    num_entries = int(data[index + 1])
    global_sum, local_sum = 0, 0

    # go deeper if no 0 encountered
    if num_leaves != 0:
        for i in range(num_leaves):
            global_sum += parse(data, index + 2)

    # sum if 0 encountered (if we are at the end of the child node)
    for i in range(num_entries):
        local_sum += int(data[index + 2 + i])

    # delete summed elements from the chain
    del data[index: index + 2 + num_entries]

    return global_sum + local_sum


def parse_value(data, index):
    num_leaves = int(data[index])
    num_entries = int(data[index + 1])
    value = 0

    if num_leaves != 0:

        # create list of all children of a given node
        children = [0]
        for i in range(num_leaves):
            children.append(parse_value(data, index + 2))

        for i in range(index + 2, index + 2 + num_entries):
            if int(data[i]) < len(children):
                value += children[int(data[i])]

    else:
        for i in range(index + 2, index + 2 + num_entries):
            value += int(data[i])

    del data[index: index + 2 + num_entries]

    return value


if __name__ == '__main__':
    input = open('inputs/input8.txt').read().split(' ')
    print('Part One: ', parse(input, 0))

    input = open('inputs/input8.txt').read().split(' ')
    print('Part Two: ', parse_value(input, 0))

