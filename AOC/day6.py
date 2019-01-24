
def distance(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def contour_coords(min_x, max_x, min_y, max_y):
    border = set()

    for x in range(min_x, max_x):
        border.add((x, min_y))
        border.add((x, max_y))
        for y in range(min_y, max_y):
            border.add((min_x, y))
            border.add((max_x, y))

    return border


def prepare_data(input):
    points, xs, ys = [], [], []

    for line in input:
        x, y = line.split(', ')
        points.append((int(x), int(y)))
        xs.append(int(x))
        ys.append(int(y))

    # return points and max and min values of x and y, to limit the terrain to a finite space
    return points, min(xs), max(xs), min(ys), max(ys)


def calculate_terrain(points, min_x, max_x, min_y, max_y):
    general_map = {}

    # for each point in the new, finite space...
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            distances = {}

            # ... calculate the distance to each of the landmarks
            for point in points:
                dist = distance((x, y), point)
                distances[point] = dist

            # then pick the landmark being the nearest
            nearest_point = min(distances, key=distances.get)
            nearest_dist = min(distances.values())

            # check if minimum occurs more than once
            del distances[nearest_point]

            # and add it to the general map (dict) as a key = a point (x, y) and
            # value = its nearest landmark ONLY if there is only one nearest landmark.
            # Otherwise add '.'
            if nearest_dist in distances.values():
                general_map[(x, y)] = '.'
            else:
                general_map[(x, y)] = nearest_point

    return general_map


def find_the_max(general_map):
    summary = {}
    for point, nearest in general_map.items():
        summary[nearest] = summary.get(nearest, 0) + 1

    border = contour_coords(min_x, max_x, min_y, max_y)
    is_true = False

    while not is_true:
        # 3) ... search for the max again.
        is_true = True
        max_point = max(summary, key=summary.get)

        # 1) check if any of the neighbours of the winning landmark crosses the border of the area ...
        for point, landmark in general_map.items():
            if landmark == max_point and point in border:
                # 2) ... if so, delete it from the dict, and ...
                del summary[max_point]
                is_true = False
                break

    return max(summary, key=summary.get), max(summary.values())


if __name__ == '__main__':

    input = open('inputs/input6.txt').read().splitlines()

    # prepare the data, points are the landmarks' coordinates
    points, min_x, max_x, min_y, max_y = prepare_data(input)

    # create the general map of all points in the are of min and max values of landmarks
    general_map = calculate_terrain(points, min_x, max_x, min_y, max_y)

    # find the solution, having checked previously some additional conditions
    biggest_landmark_coords = find_the_max(general_map)

    print('The biggest number of neighbours, less than infinity, is {}'.format(biggest_landmark_coords[1]))
