"""
Mountain Test
"""

import numpy as np
import math as math
import random as rand


def main():
    # Initializing
    rows = 3
    columns = 3
    mount_matrix = np.zeros((rows, columns))

    # Creating mountain
    drop_ones(mount_matrix)


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
    # curr_pos[0] is row position. curr_pos[1] is column position.
    while flag is True:
        print(matrix)
        # Position to check for 1s
        curr_pos = (0, middle)

        # Continue until either a 1 is hit or the ground is hit. If 1 is hit,
        # go to step 2. If ground is hit, stay in current position.
        while matrix[curr_pos] != 1 and curr_pos[0] != ground:
            curr_pos = (curr_pos[0] + 1, curr_pos[1])

        # If hit ground and position is 0, skip stability checks. Otherwise mark current position
        if not(curr_pos[0] == ground and matrix[curr_pos] == 0):
            check_stability(curr_pos, matrix, ground)
        else:
            matrix[curr_pos] = 1

        # Check if we've hit the top row.
        if curr_pos[0] == 0:
            flag = False


def check_stability(curr_pos, matrix, ground):
    """
    :param curr_pos:
    :param ground:
    :return:
    """
    # Check the 3 positions for 1s
    # one_pos is the position the 1 might be placed
    below = curr_pos
    below_left = (curr_pos[0], curr_pos[1] - 1)
    below_right = (curr_pos[0], curr_pos[1] + 1)
    one_pos = (curr_pos[0] - 1, curr_pos[1])
    spun = False
    spin = -1

    # Continue falling until hit stable position or ground.
    while not(matrix[below] == 1 and matrix[below_left] == 1 and matrix[below_right] == 1) and one_pos[0] != ground:
        # Randomly decide whether to go left or right
        if not spun:
            spin = rand.randrange(0, 2)
            spun = True

        # If spin is 1, go right. If 0, go left.
        if spin == 1:
            below = (below[0], below[1] + 1)
        else:
            below = (below[0], below[1] - 1)
        below_left = (below[0], below[1] - 1)
        below_right = (below[0], below[1] + 1)

        # If below is 0, one_pos falls
        if matrix[below] == 0:
            one_pos = below

            # If not one ground, recalculate below, below_left, and below_right
            if one_pos[0] != ground:
                below = (one_pos[0] + 1, one_pos[1])
                below_left = (one_pos[0], one_pos[1] - 1)
                below_right = (one_pos[0], one_pos[1] + 1)

        # TODO MAKE SURE BELOW AND OTHER CHECKS AREN'T OUT OF BOUNDS
        if below:
            pass

    # Mark position once stable
    matrix[one_pos] = 1









if __name__ == "__main__":
    main()