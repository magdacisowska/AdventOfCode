import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import inf


def parse():

    lines = open('inputs/input10.txt').readlines()
    data = {}

    for line in lines:
        pos, speed = line.split('> velocity=<')
        _, pos = pos.split('position=<')
        speed, _ = speed.split('>')

        x, y = pos.split(',')
        v_x, v_y = speed.split(',')

        # dictionary: key = initial coords, value = [velocity_x, velocity_y, current_x_pos, current_y_pos]
        data[int(x), -int(y)] = [int(v_x), -int(v_y), int(x), -int(y)]

    return data


def one_sec(data):

    xs, ys = [], []

    # update current positions (x, y)
    for pos, val in data.items():
        data[pos][2] += val[0]
        data[pos][3] += val[1]

        xs.append(val[2])
        ys.append(val[3])

    return data, xs, ys


def draw(data):

    xs, ys = [], []
    for pos, val in data.items():
        xs.append(val[2])
        ys.append(val[3])

    ax.clear()
    ax.scatter(xs, ys, color='g', s=150)


def animate(i, data, counter):
    data, _, _ = one_sec(data)
    draw(data)
    counter = counter + i + 2
    plt.title('{} seconds'.format(counter))


def find_text(data):
    is_found = False
    box = inf           # initial bounding box area
    counter = 0         # initial seconds counter

    while not is_found:
        # perform one second of action
        data, xs, ys = one_sec(data)

        x_range = abs(max(xs) - min(xs))
        y_range = abs(max(ys) - min(ys))

        # find the moment when we are around the smallest bounding box (2000 is arbitrary)
        if x_range * y_range + 2000 > box:
            is_found = True
        else:
            box = x_range * y_range

        counter += 1

    return data, counter


if __name__ == '__main__':
    data = parse()

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 2.5)

    data, counter = find_text(data)
    ani = animation.FuncAnimation(
        fig, animate, interval=1000, repeat=False, fargs=[data, counter])
    plt.show()
