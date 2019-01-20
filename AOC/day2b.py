import numpy as np


def find_boxes_indices(boxes):
    correct_boxes = [0, 0]
    correlation = 0
    number_of_boxes = np.size(boxes)

    for box_index in range(number_of_boxes):
        current_box = boxes[box_index]
        for ref_index in range(box_index, number_of_boxes):
            ref_box = boxes[ref_index]
            for letter in range(26):
                if current_box[letter] == ref_box[letter]:
                    correlation += 1
            if correlation == 25:
                correct_boxes = [box_index, ref_index]
                break
            correlation = 0
    return correct_boxes


def clear_strings(boxes, i, j):
    final_string = []
    for index in range(26):
        if boxes[i][index] == boxes[j][index]:
            final_string.append(boxes[j][index])
    return final_string


if __name__ == '__main__':
    inputs = open('inputs/input2.txt').read().splitlines()

    indices = find_boxes_indices(inputs)
    print('The similar strings are "{}" and "{}", located at index {} and {}'.format(inputs[indices[0]],
                                                                                     inputs[indices[1]],
                                                                                     indices[0], indices[1]))

    cleared = clear_strings(inputs, indices[0], indices[1])
    print(''.join(cleared))
