"""
Mountain Matrix
"""

import numpy as np
import math as math
import random as rand
import matplotlib.pyplot as plt


def main():
    # Initializing
    rows = 5
    columns = 5
    mount_matrix = np.zeros((rows, columns))

    # Creating mountain
    drop_ones(mount_matrix)

    # Plot circles for mountain
    # TODO FIGURE OUT WHY GRAPHING OF CIRCLES IS INCORRECT
    plot_mountain(mount_matrix)


def plot_mountain(matrix):
    # Define dimensions of the graph and of circles
    rows = np.shape(matrix)[0]
    columns = np.shape(matrix)[1]
    radius = 1
    scale = math.floor(radius // 0.5)
    plt.figure()

    # Define if rows is even or not
    if rows % 2 == 0:
        rows_even = True
    else:
        rows_even = False

    # From info in matrix, draw circles
    for curr_row in range(rows):
        prev_coords = (-1, -1)
        for curr_col in range(columns):
            if matrix[curr_row][curr_col] == 1:
                # If rows is even and the current row is even, draw circles around ones on matrix. Else draw circles between ones.
                # If rows is odd and the current row is even, draw circles between ones on matrix. Else draw circles around ones.
                coord_x = curr_row * scale
                coord_y = curr_col * scale
                if rows_even:
                    if curr_row % 2 == 0: # If current row is even
                        # Skip first one seen, then plot circles after that
                        if curr_col != 0:
                            plot_between_ones(prev_coords, coord_x, coord_y, radius)
                        # Set to last circle seen
                        prev_coords = (coord_x, coord_y)
                    # If current row is odd
                    else:
                        plot_around_ones(coord_x, coord_y, radius)
                else: # If the number of rows is odd
                    if curr_row % 2 == 0:  # If current row is even
                        # Skip first one seen, then plot circles after that
                        if curr_col != 0:
                            plot_between_ones(prev_coords, coord_x, coord_y, radius)
                        # Set to last circle seen
                        prev_coords = (coord_x, coord_y)
                    # If current row is odd
                    else:
                        plot_around_ones(coord_x, coord_y, radius)

    # Show plot
    plt.show()


def plot_between_ones(prev_coords, coord_x, coord_y, radius):
    center_x = (prev_coords[0] + coord_x) / 2
    center_y = (prev_coords[1] + coord_y) / 2
    circle = plt.Circle((center_x, center_y), radius, fc='blue')
    plt.gca().add_patch(circle)


def plot_around_ones(coord_x, coord_y, radius):
    circle = plt.Circle((coord_x, coord_y), radius, fc='blue')
    plt.gca().add_patch(circle)


def drop_ones(matrix):
    """
    right now expects odd matrix
    stable: Defined as a group of three 1s centered below the current
    position of the falling 1.
    :param matrix:
    :return:
    """
    # ground is the last row
    ground = np.shape(matrix)[0] - 1
    flag = True

    # Find middle TODO Randomize later to pick middle position when even
    middle = math.floor(len(matrix[0]) / 2)

    # 1. Drop ones until a 1 is in the top row.
    # curr_pos[0] is row position. curr_pos[1] is column position.
    while flag is True:
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
    left_wall = -1
    right_wall = np.shape(matrix)[1]
    below = curr_pos
    below_left = (curr_pos[0], curr_pos[1] - 1)
    below_right = (curr_pos[0], curr_pos[1] + 1)
    one_pos = (curr_pos[0] - 1, curr_pos[1])
    spun = False
    spin = -1

    # Continue falling until hit stable position or ground.
    while not(matrix[below] == 1 and matrix[below_left] == 1 and matrix[below_right] == 1) and one_pos[0] != ground:
        # Force 1 to fall in correct direction
        if matrix[below_right] == 0 and matrix[below_left] == 1:
            spin = 1
            spun = True
        elif matrix[below_left] == 0 and matrix[below_right] == 1:
            spin = 0
            spun = True

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
            below = (one_pos[0] + 1, one_pos[1])
            below_left = (below[0], below[1] - 1)
            below_right = (below[0], below[1] + 1)

        if below[0] > ground or below_left[1] <= left_wall or below_right[1] >= right_wall:
            break

    # Mark position once stable
    matrix[one_pos] = 1


if __name__ == "__main__":
    main()