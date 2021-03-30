import numpy as np
import time
import os


def read_matrix():
    return np.loadtxt('seed.txt', delimiter=' ', dtype='int')


def check_neighbor(matrix, x, y):
    neighbor = matrix[x % 10][(y - 1) % 10] + \
               matrix[x % 10][(y + 1) % 10] + \
               matrix[(x - 1) % 10][(y - 1) % 10] + \
               matrix[(x - 1) % 10][y % 10 % 10] + \
               matrix[(x - 1) % 10][(y + 1) % 10] + \
               matrix[(x + 1) % 10][(y - 1) % 10] + \
               matrix[(x + 1) % 10][y % 10] + \
               matrix[(x + 1) % 10][(y + 1) % 10]
    return neighbor


def survival(matrix):
    matrix_aux = np.copy(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            counter = check_neighbor(matrix, x, y)
            if matrix[x][y] == 1 and (counter < 2 or counter > 3):
                matrix_aux[x][y] = 0
            elif matrix[x][y] == 0 and counter == 3:
                matrix_aux[x][y] = 1
    return np.copy(matrix_aux)


if __name__ == '__main__':
    run = True
    matrix = read_matrix()
    while run:
        matrix = survival(matrix)
        print(matrix)
        time.sleep(0.9)
        os.system('clear')
