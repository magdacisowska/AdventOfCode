import numpy as np
from collections import deque


def play_marbles(players, last_value):

    score_board = np.zeros(players)
    circle = deque()

    # iterate through all values and act accordingly to conditions
    for i in range(last_value + 1):

        # rotate 7 to the right, perform pop() and rotate 1 left
        if i % 23 == 0 and i > 0:
            circle.rotate(7)
            score_board[i % players] += i + circle.pop()
            circle.rotate(-1)

        # rotate 1 left so the last element in list can be followed by appending the current marble
        else:
            circle.rotate(-1)
            circle.append(i)

    return score_board


if __name__ == '__main__':

    players = 411
    last_value = 71170

    print('Part One: highest score is', max(play_marbles(players, last_value)))
    print('Part Two: highest score is', max(play_marbles(players, last_value*100)))
