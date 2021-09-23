"""
Mountain Test
"""

import numpy as np
import math as math
import random as rand


def main():
    rows = 9
    columns = 9
    mount_matrix = np.zeros((rows, columns))

    # drop_ones(mount_matrix)


def drop_ones(matrix):
    """
    stable: Defined as a group of three 1s centered below the current
    position of the falling 1.
    :param matrix:
    :return:
    """
    # ground is the last row
    ground = np.shape(matrix)[0] - 1
    flag = True

    # Find middle (TODO Randomize later)
    middle = math.floor(len(matrix[0]) / 2)

    # 1. Drop ones until a 1 is in the top row.
    while flag is True:
        # Position to check for 1s
        curr_row = 0
        curr_col = middle

        # Continue until either a 1 is hit or the ground is hit. If 1 is hit,
        # go to step 2. If ground is hit, stay in current position.
        while matrix[curr_row][curr_col] != 1 or curr_row != ground:
            curr_row += 1

        # Check stability if you haven't hit the ground
        if curr_row != ground:
            curr_row, curr_col = check_stability(curr_row, curr_col, ground)

        # Mark place of ball
        matrix[curr_row][curr_col] = 1

        # Check if we've hit the top row.
        if curr_row == 0:
            flag = False


def check_stability(curr_row, curr_col, ground):
    """
    :param curr_pos:
    :param ground:
    :return:
    """
    # Check the 3 positions for 1s
    middle = curr_pos
    left = (curr_pos[0], curr_pos[1] - 1)
    right = (curr_pos[0], curr_pos[1] + 1)
    spun = False
    spin = -1

    # Continue falling until hit stable position or ground.
    while middle != 1 and left != 1 and right != 1 or curr_pos[0] != ground:
        # Randomly decide whether to go left or right
        if not spun:
            spin = rand.randrange(0, 2)
            spun = True

        # If spin is 1, go right. If 0, go left.
        if spin == 1:
            middle = (middle[0], middle[1] + 1)
        else:
            middle = (middle[0], middle[1] - 1)
        left = (middle[0], middle[1] - 1)
        right = (middle[0], middle[1] + 1)

    # If not on the ground, move the 1 on the stable formation.
    if curr_pos[0] != ground:
        middle = (middle[0] - 1, middle[1])

    return middle









if __name__ == "__main__":
    main()