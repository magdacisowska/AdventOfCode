
def sum_Z_x_Z(grid, start_x, start_y, z):
    sigma = 0

    for i in range(z):
        for j in range(z):
            sigma += grid[(start_x + i, start_y + j)]

    return sigma


def create_init_map(serial):
    map = {}

    for x in range(300):
        for y in range(300):
            rackID = x + 10
            value = (serial + y * rackID) * rackID
            hundreds = int(str(int(value / 100))[-1])
            map[(x, y)] = hundreds - 5

    return map


def first_part(map):
    powers = {}

    for x in range(297):
        for y in range(297):
            power = sum_Z_x_Z(map, x, y, 3)
            powers[(x, y, 3)] = power

    return powers


def second_part(map):
    powers_z = {}

    for x in range(300):
        for y in range(300):
            powers_z[(x, y, 1)] = map[(x, y)]
            if x < 299 and y < 299:
                powers_z[(x, y, 2)] = sum_Z_x_Z(map, x, y, 2)

    for z in range(3, 300):
        print(z, '/300')
        for x in range(300 - z):
            for y in range(300 - z):
                if x > 0 and y > 0:

                    # the same value for z-1 + new borders summed individually
                    powers_z[(x, y, z)] =\
                        sum([map.get((key, y+z-1)) for key in range(x, x+z-1)]) +\
                        sum([map.get((x+z-1, key)) for key in range(y, y+z)]) +\
                        powers_z.get((x, y, z-1))

                else:
                    powers_z[(x, y, z)] = sum_Z_x_Z(map, x, y, z)

    return powers_z


if __name__ == "__main__":
    serial = 9110
    # serial = 18

    map = create_init_map(serial)
    powers_one = first_part(map)

    powers_two = second_part(map)

    print('Part One:', max(powers_one, key=powers_one.get), max(powers_one.values()))
    print('Part Two:', max(powers_two, key=powers_two.get), max(powers_two.values()))
