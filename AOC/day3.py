import numpy as np
from collections import Counter


def decoder(inputs):
    claims = np.zeros(shape=(len(inputs), 4))

    for line in inputs:
        # pre-processing
        index, tail = line.split('@')
        margins, dims = tail.split(':')

        # extracting real data - index, margins and dimensions
        index = index.split('#')[1]
        margin_left, margin_up = margins.split(',')
        dim_x, dim_y = dims.split('x')

        claims[int(index) - 1][0:4] = margin_left, margin_up, dim_x, dim_y

    return claims


def find_duplicates(claims):
    occupied_squares = []

    for index in range(len(claims)):

        margin_left = int(claims[index][0])
        margin_up = int(claims[index][1])
        dim_x = int(claims[index][2])
        dim_y = int(claims[index][3])

        # create string pairs 'x-y' of busy squares
        for y in range(dim_y):
            for x in range(dim_x):
                occupied_squares.append(str(margin_left + x) + '-' + str(margin_up + y))

    # iterates through pairs 'x-y', counting the number of recurrent ones
    dupes = [item for item, count in Counter(occupied_squares).items() if count > 1]

    return dupes, len(dupes)


def find_the_one(claims, dupes):

    for index in range(len(claims)):
        print(index)
        is_interfering = False

        margin_left = int(claims[index][0])
        margin_up = int(claims[index][1])
        dim_x = int(claims[index][2])
        dim_y = int(claims[index][3])

        for y in range(dim_y):
            for x in range(dim_x):
                coords = str(margin_left + x) + '-' + str(margin_up + y)
                if coords in dupes:
                    is_interfering = True
                    break
                elif y == dim_y - 1 and x == dim_x - 1 and is_interfering is False:
                    return index + 1

    return None


if __name__ == '__main__':

    inputs = open('inputs/input3.txt').read().splitlines()

    claims = decoder(inputs)
    dupes, num_of_dupes = find_duplicates(claims)

    print('Number of duplicated (or more) square inches: {}'.format(num_of_dupes))
    print('The one not interfering has the index of '.format(find_the_one(claims, dupes)))
